import json
import pickle
from datetime import datetime

import numpy as np
import tensorflow as tf
import torch

from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sqlalchemy import create_engine, Table, Column, Integer, Float, String, Text, DateTime, MetaData
import h5py

app = FastAPI()

DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/comments_db"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

comments = Table(
    "comments",
    metadata,
    autoload_with=engine
)


print("Loading models...")

# CNN toxicity model
with h5py.File("cnn_toxicity.h5", "r+") as f:
    model_config = f.attrs["model_config"]
    if isinstance(model_config, bytes):
        model_config = model_config.decode()
    model_config = json.loads(model_config)
    for layer in model_config["config"]["layers"]:
        if "config" in layer and "quantization_config" in layer["config"]:
            layer["config"].pop("quantization_config")
    f.attrs["model_config"] = json.dumps(model_config)

cnn_model = tf.keras.models.load_model("cnn_toxicity.h5", compile=False)

# tokenizer CNN
with open("tokenizer_tox.pkl", "rb") as f:
    tokenizer_tox = pickle.load(f)

MAX_LEN = 84

# RuBERT sentiment
with open("streamlit_model/config.json") as f:
    config = json.load(f)

sent_tokenizer = AutoTokenizer.from_pretrained(config["tokenizer_path"])
sent_model = AutoModelForSequenceClassification.from_pretrained(config["model_path"])
label_map = config["labels"]
max_length = config["max_length"]
sent_model.eval()

print("Models loaded")


class Comment(BaseModel):
    comment: str


def predict_toxicity(text):
    seq = tokenizer_tox.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=MAX_LEN)
    pred = cnn_model.predict(padded)[0][0]
    return float(pred)


def predict_sentiment(text):
    inputs = sent_tokenizer(
        text,
        truncation=True,
        padding=True,
        max_length=max_length,
        return_tensors="pt"
    )
    with torch.no_grad():
        outputs = sent_model(**inputs)
    probs = torch.softmax(outputs.logits, dim=1)
    score = torch.max(probs).item()
    label_id = torch.argmax(probs).item()
    label = label_map[label_id]
    return label, float(score)


@app.post("/analyze")
def analyze(data: Comment):
    text = data.comment

    toxicity = predict_toxicity(text)
    sentiment_label, sentiment_score = predict_sentiment(text)

    record = {
        "text": text,
        "toxicity": round(toxicity, 3),
        "sentiment": sentiment_label,
        "created_at": datetime.now()
    }

    with engine.begin() as conn:
        res = conn.execute(comments.insert().values(**record))
        record["id"] = res.inserted_primary_key[0]

    return record
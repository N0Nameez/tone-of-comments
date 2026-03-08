# 📊 Comment Analysis: Toxicity & Sentiment

Automated comment analysis system for detecting toxicity and sentiment in Russian text using machine learning models.

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Model Performance](#model-performance)
- [Tech Stack](#tech-stack)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Interpreting Results](#interpreting-results)
- [Notes](#Notes)
- [Authors](#authors)

---

## 📝 About

This project is a web application for comment analysis that determines:

1. **Toxicity** — Probability that a comment contains insults, threats, or negative content (CNN model)
2. **Sentiment** — Emotional tone of the text: positive, negative, or neutral (RuBERT model)

Analysis results are stored in a MySQL database for monitoring and statistics.

> ⚠️ **Note:** This is an educational project created for learning purposes.

---

## ✨ Features

- 🔍 Toxicity detection (0–1 scale)
- 🎯 Sentiment classification (positive/negative/neutral)
- 💾 Results persistence in MySQL database
- 🖥️ User-friendly Streamlit web interface
- 🚀 REST API for third-party integration
- 🇷🇺 Russian language support

---

## 📈 Model Performance

### Toxicity Model (CNN)

| Metric | Score |
|--------|-------|
| Accuracy | 0.8848 |
| F1-Score (Macro Avg) | 0.8708 |

### Sentiment Model (RuBERT)

| Metric | Score |
|--------|-------|
| Accuracy | 0.8079 |
| F1-Score (Macro Avg) | 0.8067 |

---

## 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| Backend | FastAPI |
| Frontend | Streamlit |
| Toxicity Model | TensorFlow + CNN |
| Sentiment Model | PyTorch + RuBERT |
| Database | MySQL |
| Tokenization | Transformers (Hugging Face) |
| API Documentation | Swagger/OpenAPI |

---

## 📦 Requirements

```txt
fastapi
uvicorn
streamlit
transformers
torch
tensorflow-cpu
sqlalchemy
pymysql
```

## 🚀 Installation
1. Clone the Repository

```txt
git clone https://github.com/N0Nameez/study_repo.git
cd study_repo/4_course/tone_comments
```

2. Create Virtual Environment

```txt
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Dependencies

```txt
pip install -r requirements.txt
```

4. Set Up Database
Create MySQL database and table:

```txt
CREATE DATABASE comments_db;
USE comments_db;

CREATE TABLE comments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    text TEXT NOT NULL,
    toxicity FLOAT,
    sentiment VARCHAR(50),
    created_at DATETIME
);
```

5. Configure Database Connection
Update api.py with your credentials:

```txt
DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/comments_db"
```

6. Verify Model Files
Ensure the following files are present in the project directory:

```txt
cnn_toxicity.h5           # CNN model for toxicity
tokenizer_tox.pkl         # CNN tokenizer
streamlit_model/
    config.json           # RuBERT configuration
```

## 🏃 Usage
1. Start API Server

```txt
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

2. Start Streamlit Interface (new terminal)

```txt
streamlit run main.py
```

3. Open in Browser

## 📁 Project Structure

```txt
tone-of-comments/
├── api.py                    # FastAPI backend server
├── main.py                   # Streamlit frontend interface
├── cnn_toxicity.h5           # Trained CNN model (toxicity)
├── tokenizer_tox.pkl         # Tokenizer for CNN model
├── streamlit_model/
│   └── config.json           # RuBERT model configuration
├── requirements.txt          # Python dependencies
├── tone_of_comments.ipynb    # Jupyter notebook (training/analysis)
└── README.md                 # Project documentation
```

## 📊 Interpreting Results
Toxicity Score

| Range | Color | Meaning |
|-------|-------|---------|
| 0.0 – 0.3 | 🟢 Green | Low toxicity (safe) |
| 0.3 – 0.7 | 🟠 Orange | Moderate toxicity (review needed) |
| 0.7 – 1.0 | 🔴 Red | High toxicity (block/reject) |

Sentiment Labels

| Label | Color | Description |
|-------|-------|-------------|
| positive | 🟢 Green | Positive sentiment |
| negative | 🔴 Red | Negative sentiment |
| neutral | ⚪ Gray | Neutral sentiment |

## 📝 Notes
This is an educational project — not intended for production use
Models are trained on Russian language data
No Docker deployment available (run locally)
No automated tests included
No license specified (educational use only)

## 👥 Authors
N0Nameez — GitHub Profile

<div align="center">

If you found this project helpful, please give it a ⭐ on GitHub!
Made with ❤️ for Russian NLP community
Educational Project — 2026
</div>
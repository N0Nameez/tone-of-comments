import streamlit as st
import requests

st.title("Анализ комментариев: токсичность и тональность")

comment = st.text_area("Введите комментарий:")

def color_for_toxicity(score):
    if score < 0.3:
        return "green"
    elif score < 0.7:
        return "orange"
    else:
        return "red"

def color_for_sentiment(label):
    if label.lower() == "positive":
        return "green"
    elif label.lower() == "negative":
        return "red"
    else:
        return "gray"

if st.button("Анализировать"):
    if not comment.strip():
        st.warning("Введите текст комментария")
    else:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/analyze",
                json={"comment": comment}
            )
            data = response.json()

            if "error" in data:
                st.error(f"Ошибка API: {data['error']}")
            else:
                st.subheader("Результаты")

                tox_color = color_for_toxicity(data['toxicity'])
                sent_color = color_for_sentiment(data['sentiment'])

                st.markdown(f"**Токсичность:** <span style='color:{tox_color}'>{data['toxicity']:.3f}</span>", unsafe_allow_html=True)
                st.markdown(f"**Тональность:** <span style='color:{sent_color}'>{data['sentiment']}</span>", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Ошибка запроса: {e}")
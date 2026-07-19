# 📊 Анализ комментариев: Токсичность и Тональность

Автоматизированная система анализа комментариев для определения токсичности и тональности русскоязычного текста с использованием моделей машинного обучения.

## 📋 Оглавление

- [О проекте](#-о-проекте)
- [Особенности](#-особенности)
- [Производительность моделей](#-производительность-моделей)
- [Стек технологий](#-стек-технологий)
- [Требования](#-требования)
- [Установка](#-установка)
- [Использование](#-использование)
- [Структура проекта](#-структура-проекта)
- [Интерпретация результатов](#-интерпретация-результатов)
- [Примечания](#-примечания)
- [Авторы](#-авторы)

---

## 📝 О проекте

Данный проект представляет собой веб-приложение для анализа комментариев, которое определяет:

1. **Токсичность** — Вероятность того, что комментарий содержит оскорбления, угрозы или негативный контент (модель CNN)
2. **Тональность** — Эмоциональная окраска текста: позитивная, негативная или нейтральная (модель RuBERT)

Результаты анализа сохраняются в базу данных MySQL для мониторинга и сбора статистики.

> ⚠️ **Примечание:** Это учебный проект, созданный в образовательных целях.

---

## ✨ Особенности

- 🔍 Определение токсичности (шкала от 0 до 1)
- 🎯 Классификация тональности (позитивная/негативная/нейтральная)
- 💾 Сохранение результатов в базу данных MySQL
- 🖥️ Удобный веб-интерфейс на базе Streamlit
- 🚀 REST API для сторонних интеграций
- 🇷🇺 Поддержка русского языка

---

## 📈 Производительность моделей

### Модель токсичности (CNN)

| Метрика | Значение |
|---------|----------|
| Точность (Accuracy) | 0.8848 |
| F1-Score (Macro Avg) | 0.8708 |

### Модель тональности (RuBERT)

| Метрика | Значение |
|---------|----------|
| Точность (Accuracy) | 0.8079 |
| F1-Score (Macro Avg) | 0.8067 |

---

## 🛠 Стек технологий

| Компонент | Технология |
|-----------|------------|
| Backend | FastAPI |
| Frontend | Streamlit |
| Модель токсичности | TensorFlow + CNN |
| Модель тональности | PyTorch + RuBERT |
| База данных | MySQL |
| Токенизация | Transformers (Hugging Face) |
| Документация API | Swagger/OpenAPI |

---

## 📦 Требования

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

## 🚀 Установка
1. Клонируйте репозиторий

```bash
git clone [https://github.com/N0Nameez/study_repo.git](https://github.com/N0Nameez/study_repo.git)
cd study_repo/4_course/tone_comments
```

2. Создайте виртуальное окружение

```bash
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
```

3. Установите зависимости

```bash
pip install -r requirements.txt
```

4. Настройте базу данных
Создайте базу данных MySQL и таблицу:

```sql
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

5. Настройте подключение к БД
Обновите файл api.py, указав ваши учетные данные:

```python
DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/comments_db"
```

6. Проверьте файлы моделей
Убедитесь, что в директории проекта присутствуют следующие файлы:

```txt
cnn_toxicity.h5           # CNN модель для токсичности
tokenizer_tox.pkl         # Токенизатор для CNN
streamlit_model/
    config.json           # Конфигурация модели RuBERT
```

## 🏃 Использование
1. Запустите API сервер

```bash
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

2. Запустите интерфейс Streamlit (в новом терминале)

```bash
streamlit run main.py
```

3. Откройте в браузере

## 📁 Структура проекта

```txt
tone-of-comments/
├── api.py                    # Backend-сервер на FastAPI
├── main.py                   # Frontend-интерфейс на Streamlit
├── cnn_toxicity.h5           # Обученная CNN модель (токсичность)
├── tokenizer_tox.pkl         # Токенизатор для CNN модели
├── streamlit_model/
│   └── config.json           # Конфигурация модели RuBERT
├── requirements.txt          # Python-зависимости
├── tone_of_comments.ipynb    # Jupyter ноутбук (обучение/анализ)
└── README.md                 # Документация проекта
```

## 📊 Интерпретация результатов
Оценка токсичности (Toxicity Score)

| Диапазон | Цвет | Значение |
|----------|------|----------|
| 0.0 – 0.3 | 🟢 Зеленый | Низкая токсичность (безопасно) |
| 0.3 – 0.7 | 🟠 Оранжевый | Умеренная токсичность (требуется проверка) |
| 0.7 – 1.0 | 🔴 Красный | Высокая токсичность (блокировка/отклонение) |

Метки тональности (Sentiment Labels)

| Метка | Цвет | Описание |
|-------|------|----------|
| positive | 🟢 Зеленый | Позитивная тональность |
| negative | 🔴 Красный | Негативная тональность |
| neutral | ⚪ Серый | Нейтральная тональность |

## 📝 Примечания
Это образовательный проект — не предназначен для использования в продакшене.
Модели обучены на русскоязычных данных.
Деплой через Docker не предусмотрен (запуск локально).
Автоматические тесты не включены.
Лицензия не указана (только для образовательного использования).

## 👥 Авторы

**Влад** — [N0Nameez](https://github.com/N0Nameez)

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/N0Nameez)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/vladeveloper)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:fedenev.vladis@yandex.com)

<div align="center">

**Репозиторий:** [github.com/N0Nameez/study_repo/tree/main/4_course/tone_comments](https://github.com/N0Nameez/study_repo/tree/main/4_course/tone_comments)

Если этот проект оказался вам полезен, пожалуйста, поставьте ⭐ на GitHub!
Сделано с ❤️ для русскоязычного NLP-сообщества
</div>

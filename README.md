# Sentiment Analyzer

An end-to-end NLP system that classifies tweet sentiments as Positive, Negative or Neutral using Multinomial Naive Bayes, SpaCy, VADER, FastAPI and Streamlit.

# Problem Statement

Every day people share thousands of opinions on Twitter about airlines, products, movies, restaurants and many more which is impossible to read manually. This project automatically analyzes any tweet and tells whether the feeling behind it is positive, negative or neutral.

# Features

 ✅ Classifies tweets as **Positive**, **Negative** or **Neutral**
 ✅ Shows **Compound Score** using VADER
 ✅ Handles **negation** — "not good" is treated as negative
 ✅ **Single tweet** analysis
 ✅ **Batch analysis** — multiple tweets at once
 ✅ **Confidence scores** with bar chart
 ✅ **VADER gauge** visualization
 ✅ REST API with FastAPI
 ✅ Interactive dashboard with Streamlit

# Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| Preprocessing | SpaCy + Regex |
| Sentiment Scoring | VADER |
| Feature Extraction | TF-IDF |
| ML Model | Multinomial Naive Bayes |
| ML Pipeline | Scikit-learn |
| Model Storage | Joblib |
| Backend | FastAPI + Uvicorn |
| Frontend | Streamlit + Plotly |
| Version Control | Git + GitHub |


# Project Structure
-----
```
sentiment-analysis/
│
├── backend/
│   ├── src/
│   │   ├── preprocess.py        # Tweet cleaning + VADER scoring
│   │   ├── train.py             # Model training pipeline
│   │   └── predict.py           # Combined prediction logic
│   ├── models/
│   │   └── sentiment_model.pkl  # Saved trained model
│   ├── data/
│   │   └── tweets.csv           # Dataset (not included)
│   ├── notebooks/
│   │   └── exploration.ipynb    # EDA notebook
│   ├── api.py                   # FastAPI entry point
│   └── requirements.txt         # Backend dependencies
│
├── frontend/
│   ├── app.py                   # Streamlit main app
│   ├── components/
│   │   ├── charts.py            # Plotly chart components
│   │   └── ui.py                # Reusable UI components
│   └── requirements.txt         # Frontend dependencies
│
├── .gitignore
└── README.md
```

---

# Dataset

- Name: Twitter US Airline Sentiment
- Source: [Kaggle](https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment)
- Size:14,640 tweets
- Classes: Negative, Neutral, Positive

| Label | Count |
|---|---|
| Negative | 9,178 |
| Neutral | 3,099 |
| Positive | 2,363 |

---

# How It Works

```
Input Tweet
     ↓
Clean Text (remove URLs, mentions, hashtags)
     ↓
SpaCy Lemmatization + Negation Handling
     ↓
TF-IDF Vectorization
     ↓
Multinomial Naive Bayes  →  60% weight
VADER Compound Score     →  40% weight
     ↓
Combined Final Prediction
     ↓
Negative / Neutral / Positive
```

---

# Setup & Installation

# 1. Clone the repository
```bash
git clone https://github.com/maheshchithini-dotcom/Sentiment-Analyzer.git
cd Sentiment-Analyzer
```

# 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

# 3. Install backend dependencies
```bash
cd backend
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

# 4. Download dataset
- Download from [Kaggle](https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment)
- Place the file as `backend/data/tweets.csv`

# 5. Train the model
```bash
cd backend/src
python train.py
```

# 6. Start backend API
```bash
cd backend
uvicorn api:app --reload --port 8000
```

# 7. Install frontend dependencies
```bash
cd frontend
pip install -r requirements.txt
```

# 8. Start frontend
```bash
streamlit run app.py
```

---

# API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| POST | `/predict` | Single tweet prediction |
| POST | `/predict/batch` | Batch tweet prediction |

### Example Request
```json
POST http://localhost:8000/predict
{
  "text": "I love this airline, best flight ever!"
}
```

### Example Response
```json
{
  "input": "I love this airline, best flight ever!",
  "label": "positive",
  "confidence": {
    "negative": 0.04,
    "neutral": 0.11,
    "positive": 0.85
  },
  "compound_score": 0.8316,
  "vader_scores": {
    "compound": 0.8316,
    "positive": 0.538,
    "neutral": 0.462,
    "negative": 0.0
  }
}
```

---

## 📈 Model Performance

| Metric | Score |
|---|---|
| Accuracy | ~85% |
| Negative F1 | 0.88 |
| Neutral F1 | 0.77 |
| Positive F1 | 0.82 |

---

## 🖥️ Dashboard

| Feature | Description |
|---|---|
| Single Tweet Tab | Analyze one tweet at a time |
| Batch Analysis Tab | Analyze multiple tweets at once |
| Confidence Chart | Bar chart showing class probabilities |
| VADER Gauge | Compound score meter from -1 to +1 |
| Sentiment Card | Color coded result display |

---

##  Future Improvements

- Add support for CSV file upload
- Deploy on cloud (AWS / Heroku / Render)
- Add multilingual support
- Integrate live Twitter/X API
- Add history tracking dashboard

---


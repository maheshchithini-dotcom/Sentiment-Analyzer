import os
import sys
import joblib

sys.path.append(os.path.dirname(__file__))
from preprocess import preprocess, get_vader_score

MODEL_PATH = os.path.join(os.path.dirname(__file__), "../models/sentiment_model.pkl")

pipeline = joblib.load(MODEL_PATH)


def predict(text: str) -> dict:
    clean = preprocess(text)
    proba = pipeline.predict_proba([clean])[0]
    classes = pipeline.classes_

    # Model confidence scores
    model_scores = {
        cls: round(float(prob), 4)
        for cls, prob in zip(classes, proba)
    }

    # VADER scores
    vader = get_vader_score(text)
    compound = vader["compound"]

    # Combine — 60% model + 40% VADER
    combined = {
        "negative": round(model_scores["negative"] * 0.6 + (1 - (compound + 1) / 2) * 0.4, 4),
        "neutral":  round(model_scores["neutral"]  * 0.6 + (1 - abs(compound)) * 0.4, 4),
        "positive": round(model_scores["positive"] * 0.6 + ((compound + 1) / 2) * 0.4, 4),
    }

    # Final label
    label = max(combined, key=combined.get)

    return {
        "label": label,
        "confidence": combined,
        "compound_score": compound,
        "vader_scores": vader,
    }

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.predict import predict

app = FastAPI(
    title="Sentiment Analysis API",
    description="Analyzes tweet sentiment — Negative, Neutral, or Positive",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class TextInput(BaseModel):
    text: str


class BatchInput(BaseModel):
    texts: list[str]


@app.get("/")
def root():
    return {"message": "Sentiment Analysis API is running!"}


@app.post("/predict")
def predict_sentiment(input: TextInput):
    if not input.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
    result = predict(input.text)
    return {
        "input": input.text,
        "label": result["label"],
        "confidence": result["confidence"],
        "compound_score": result["compound_score"],
        "vader_scores": result["vader_scores"],
    }


@app.post("/predict/batch")
def predict_batch(input: BatchInput):
    if not input.texts:
        raise HTTPException(status_code=400, detail="Texts list cannot be empty.")
    results = []
    for text in input.texts:
        result = predict(text)
        results.append({
            "input": text,
            "label": result["label"],
            "confidence": result["confidence"],
            "compound_score": result["compound_score"],
        })
    return {"results": results}
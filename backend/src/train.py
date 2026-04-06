import os
import sys
import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.utils import resample

sys.path.append(os.path.dirname(__file__))
from preprocess import preprocess


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, encoding="latin-1")
    df = df[["airline_sentiment", "text"]].dropna()
    df.columns = ["label", "text"]
    return df


def balance_data(df: pd.DataFrame) -> pd.DataFrame:
    # Balance all classes to same size as majority class
    max_size = df["label"].value_counts().max()
    balanced = []
    for label in df["label"].unique():
        subset = df[df["label"] == label]
        upsampled = resample(subset, replace=True, n_samples=max_size, random_state=42)
        balanced.append(upsampled)
    return pd.concat(balanced).sample(frac=1, random_state=42).reset_index(drop=True)


def train():
    data_path = os.path.join(os.path.dirname(__file__), "../data/tweets.csv")
    model_path = os.path.join(os.path.dirname(__file__), "../models/sentiment_model.pkl")

    print("Loading data...")
    df = load_data(data_path)
    print(f"Total samples: {len(df)}")
    print(f"Label distribution:\n{df['label'].value_counts()}\n")

    print("Balancing classes...")
    df = balance_data(df)
    print(f"Balanced distribution:\n{df['label'].value_counts()}\n")

    print("Preprocessing tweets...")
    df["clean_text"] = df["text"].apply(preprocess)

    X = df["clean_text"]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    print(f"Train size: {len(X_train)} | Test size: {len(X_test)}\n")

    print("Training pipeline...")
    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(
            max_features=15000,
            ngram_range=(1, 3),   # unigrams + bigrams + trigrams
            sublinear_tf=True,
            min_df=2
        )),
        ("model", MultinomialNB(alpha=0.3))
    ])

    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)

    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}\n")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    joblib.dump(pipeline, model_path)
    print(f"\nModel saved to: {model_path}")


if __name__ == "__main__":
    train()
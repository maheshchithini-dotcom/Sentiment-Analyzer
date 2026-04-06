import re
import spacy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

nlp = spacy.load("en_core_web_sm")
analyzer = SentimentIntensityAnalyzer()

NEGATIONS = {
    "not", "no", "never", "neither", "nor",
    "hardly", "barely", "doesn't", "isn't",
    "wasn't", "wouldn't", "couldn't", "shouldn't",
    "don't", "won't", "cant", "cannot", "nothing",
    "nobody", "nowhere", "without", "lack"
}


def clean_tweet(text: str) -> str:
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#\w+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def lemmatize(text: str) -> str:
    doc = nlp(text)
    tokens = []
    negate = False

    for token in doc:
        if token.is_punct:
            negate = False
            continue

        word = token.lemma_.lower()

        if word in NEGATIONS:
            negate = True
            tokens.append(word)
            continue

        if token.is_stop:
            continue

        if negate:
            tokens.append(f"not_{word}")
            negate = False
        else:
            tokens.append(word)

    return " ".join(tokens)


def preprocess(text: str) -> str:
    cleaned = clean_tweet(text)
    lemmatized = lemmatize(cleaned)
    return lemmatized


def get_vader_score(text: str) -> dict:
    scores = analyzer.polarity_scores(text)
    return {
        "compound": round(scores["compound"], 4),
        "positive": round(scores["pos"], 4),
        "neutral":  round(scores["neu"], 4),
        "negative": round(scores["neg"], 4),
    }
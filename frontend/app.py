import requests
import streamlit as st

from components.charts import confidence_chart, vader_gauge
from components.ui import (
    inject_global_styles,
    render_hero,
    section_title,
    sentiment_badge,
    show_result_card,
)

API_URL = "http://localhost:8000/predict"
BATCH_URL = "http://localhost:8000/predict/batch"

st.set_page_config(
    page_title="Tweet Sentiment Analyzer",
    page_icon="💬",
    layout="wide",
)

inject_global_styles()
render_hero()

tab1, tab2 = st.tabs(["Single Tweet", "Batch Analysis"])

with tab1:
    section_title("Type a tweet")
    user_input = st.text_area(
        "Enter a tweet:",
        placeholder="Share a tweet and we will map its overall sentiment...",
        height=140,
        label_visibility="collapsed",
    )

    if st.button("Analyze Sentiment", use_container_width=True, key="single"):
        if user_input.strip():
            with st.spinner("Analyzing sentiment..."):
                response = requests.post(API_URL, json={"text": user_input}, timeout=30)
                response.raise_for_status()
                data = response.json()

            label = data["label"]
            compound = data["compound_score"]
            confidence = data["confidence"]
            vader = data["vader_scores"]

            left_col, right_col = st.columns([1.05, 0.95], gap="large")
            with left_col:
                section_title("Prediction")
                show_result_card(label, compound)

            with right_col:
                section_title("Confidence Scores")
                st.plotly_chart(confidence_chart(confidence), use_container_width=True)

            section_title("VADER Breakdown")
            st.plotly_chart(vader_gauge(vader), use_container_width=True)
        else:
            st.warning("Please enter some text before running the analysis.")

with tab2:
    section_title("Analyze multiple tweets")
    batch_input = st.text_area(
        "Enter multiple tweets (one per line):",
        placeholder="Tweet 1\nTweet 2\nTweet 3",
        height=220,
        label_visibility="collapsed",
    )

    if st.button("Analyze Batch", use_container_width=True, key="batch"):
        texts = [tweet.strip() for tweet in batch_input.strip().split("\n") if tweet.strip()]
        if texts:
            with st.spinner(f"Analyzing {len(texts)} tweets..."):
                response = requests.post(BATCH_URL, json={"texts": texts}, timeout=60)
                response.raise_for_status()
                data = response.json()

            section_title("Batch Results")
            for item in data["results"]:
                with st.expander(f"{sentiment_badge(item['label'])}  {item['input'][:80]}"):
                    metric_col1, metric_col2, metric_col3 = st.columns(3)
                    metric_col1.metric("Label", item["label"].upper())
                    metric_col2.metric("Compound Score", f"{item['compound_score']:.4f}")
                    metric_col3.metric(
                        "Confidence",
                        f"{max(item['confidence'].values()):.2%}",
                    )
        else:
            st.warning("Please enter at least one tweet for batch analysis.")

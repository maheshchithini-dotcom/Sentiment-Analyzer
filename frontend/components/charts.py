
import plotly.graph_objects as go


def confidence_chart(confidence: dict) -> go.Figure:
    labels = list(confidence.keys())
    values = list(confidence.values())

    color_map = {
        "negative": "#ef4444",
        "neutral":  "#facc15",
        "positive": "#22c55e",
    }
    colors = [color_map.get(l, "#888") for l in labels]

    fig = go.Figure(go.Bar(
        x=labels,
        y=values,
        marker_color=colors,
        marker_line_color="rgba(248,250,252,0.12)",
        marker_line_width=1.2,
        text=[f"{v:.2%}" for v in values],
        textposition="outside",
        hovertemplate="%{x}: %{y:.2%}<extra></extra>",
    ))

    fig.update_layout(
        yaxis=dict(
            title=dict(text="Probability", font=dict(color="#e2e8f0")),
            range=[0, 1],
            gridcolor="rgba(148, 163, 184, 0.18)",
            zeroline=False,
            tickfont=dict(color="#cbd5e1"),
        ),
        xaxis=dict(
            tickfont=dict(color="#e2e8f0", size=14),
            showgrid=False,
        ),
        height=320,
        margin=dict(l=10, r=10, t=10, b=10),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#f8fafc"),
    )
    return fig


def vader_gauge(vader: dict) -> go.Figure:
    compound = vader["compound"]

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=compound,
        number={"font": {"size": 34, "color": "#f8fafc"}},
        gauge={
            "axis": {
                "range": [-1, 1],
                "tickcolor": "#cbd5e1",
                "tickfont": {"color": "#e2e8f0"},
            },
            "bar": {"color": "#38bdf8", "thickness": 0.34},
            "steps": [
                {"range": [-1, -0.05], "color": "#3a1418"},
                {"range": [-0.05, 0.05], "color": "#3f3310"},
                {"range": [0.05, 1], "color": "#0d3420"},
            ],
            "threshold": {
                "line": {"color": "#f8fafc", "width": 4},
                "thickness": 0.75,
                "value": compound,
            },
        },
        title={"text": "Compound Sentiment Score", "font": {"color": "#f8fafc", "size": 16}},
    ))

    fig.update_layout(
        height=290,
        margin=dict(l=20, r=20, t=40, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#f8fafc"),
    )
    return fig

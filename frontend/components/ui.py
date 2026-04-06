import streamlit as st

ICON_MAP = {
    "positive": "+",
    "neutral": "~",
    "negative": "-",
}

COLOR_MAP = {
    "positive": "#22c55e",
    "neutral": "#facc15",
    "negative": "#ef4444",
}

GLOW_MAP = {
    "positive": "rgba(34, 197, 94, 0.28)",
    "neutral": "rgba(250, 204, 21, 0.24)",
    "negative": "rgba(239, 68, 68, 0.24)",
}


def inject_global_styles() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Manrope:wght@400;500;600;700&display=swap');

        :root {
            --bg: #0b1020;
            --panel: rgba(13, 19, 38, 0.82);
            --panel-border: rgba(148, 163, 184, 0.18);
            --text: #f8fafc;
            --muted: #94a3b8;
            --accent: #38bdf8;
        }

        .stApp {
            background:
                radial-gradient(circle at top left, rgba(56, 189, 248, 0.16), transparent 30%),
                radial-gradient(circle at top right, rgba(14, 165, 233, 0.14), transparent 26%),
                linear-gradient(180deg, #09101d 0%, #0b1020 48%, #050814 100%);
            color: var(--text);
        }

        .stApp, .stMarkdown, .stText, .stButton button, .stTextArea textarea, .stTabs, .stMetric {
            font-family: "Manrope", sans-serif;
        }

        h1, h2, h3 {
            font-family: "Space Grotesk", sans-serif !important;
            letter-spacing: -0.03em;
        }

        section.main > div {
            padding-top: 2rem;
        }

        .block-container {
            max-width: 1220px;
            padding-top: 0.5rem;
            padding-bottom: 3rem;
        }

        .hero-shell {
            position: relative;
            overflow: hidden;
            padding: 2rem;
            border: 1px solid rgba(125, 211, 252, 0.18);
            border-radius: 28px;
            background:
                linear-gradient(135deg, rgba(15, 23, 42, 0.92), rgba(10, 15, 31, 0.78)),
                rgba(15, 23, 42, 0.9);
            box-shadow: 0 24px 80px rgba(2, 8, 23, 0.45);
        }

        .hero-shell::before {
            content: "";
            position: absolute;
            inset: auto -8% -45% auto;
            width: 280px;
            height: 280px;
            border-radius: 999px;
            background: radial-gradient(circle, rgba(34, 211, 238, 0.28), transparent 66%);
        }

        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.55rem;
            padding: 0.4rem 0.8rem;
            border: 1px solid rgba(125, 211, 252, 0.18);
            border-radius: 999px;
            color: #bae6fd;
            background: rgba(14, 165, 233, 0.08);
            font-size: 0.88rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
        }

        .hero-title {
            margin: 1rem 0 0.8rem;
            font-size: clamp(2.3rem, 5vw, 4rem);
            line-height: 1;
            color: #f8fafc;
        }

        .hero-subtitle {
            max-width: 760px;
            margin: 0;
            color: #cbd5e1;
            font-size: 1.05rem;
            line-height: 1.7;
        }

        .info-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 1rem;
            margin-top: 1.5rem;
        }

        .info-card {
            padding: 1rem 1.1rem;
            border-radius: 20px;
            border: 1px solid rgba(148, 163, 184, 0.14);
            background: rgba(15, 23, 42, 0.58);
            backdrop-filter: blur(10px);
        }

        .info-card span {
            display: block;
            color: #7dd3fc;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }

        .info-card strong {
            display: block;
            margin-top: 0.45rem;
            color: #f8fafc;
            font-size: 1rem;
            font-weight: 700;
        }

        div[data-testid="stTabs"] button[role="tab"] {
            min-height: 52px;
            padding: 0.55rem 1.1rem;
            border-radius: 14px 14px 0 0;
            color: #cbd5e1;
            font-weight: 700;
        }

        div[data-testid="stTabs"] button[role="tab"][aria-selected="true"] {
            color: #f8fafc;
            background: linear-gradient(180deg, rgba(14, 165, 233, 0.18), rgba(14, 165, 233, 0.04));
        }

        div[data-testid="stTabs"] div[role="tabpanel"] {
            padding-top: 1rem;
        }

        .panel-title {
            margin: 0 0 0.85rem;
            color: #f8fafc;
            font-size: 1.15rem;
            font-weight: 700;
        }

        div[data-testid="stTextArea"] textarea {
            min-height: 140px;
            border-radius: 22px;
            border: 1px solid rgba(148, 163, 184, 0.2);
            background: rgba(15, 23, 42, 0.82);
            color: #f8fafc;
            font-size: 1rem;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.02);
        }

        div[data-testid="stTextArea"] textarea:focus {
            border-color: rgba(56, 189, 248, 0.68);
            box-shadow: 0 0 0 1px rgba(56, 189, 248, 0.32);
        }

        .stButton button {
            height: 3.4rem;
            border: 0;
            border-radius: 18px;
            color: #eff6ff;
            font-size: 1rem;
            font-weight: 800;
            background: linear-gradient(135deg, #0ea5e9, #2563eb);
            box-shadow: 0 18px 40px rgba(37, 99, 235, 0.28);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .stButton button:hover {
            transform: translateY(-1px);
            box-shadow: 0 22px 44px rgba(14, 165, 233, 0.3);
        }

        div[data-testid="stExpander"] {
            border: 1px solid rgba(148, 163, 184, 0.14);
            border-radius: 18px;
            background: rgba(15, 23, 42, 0.72);
            overflow: hidden;
        }

        div[data-testid="stMetric"] {
            border: 1px solid rgba(148, 163, 184, 0.14);
            border-radius: 18px;
            padding: 0.9rem 1rem;
            background: rgba(15, 23, 42, 0.72);
        }

        @media (max-width: 900px) {
            .hero-shell {
                padding: 1.4rem;
            }

            .info-grid {
                grid-template-columns: 1fr;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_hero() -> None:
    st.markdown(
        """
        <section class="hero-shell">
            <div class="hero-badge">Live Sentiment Studio</div>
            <h1 class="hero-title">Tweet Sentiment Analyzer</h1>
            <p class="hero-subtitle">
                Turn raw tweets into clear sentiment signals with a cleaner, more visual dashboard for single-text
                checks and quick batch analysis.
            </p>
            <div class="info-grid">
                <div class="info-card">
                    <span>Prediction Modes</span>
                    <strong>Single tweet and batch workflows</strong>
                </div>
                <div class="info-card">
                    <span>Outputs</span>
                    <strong>Label, confidence, and VADER breakdown</strong>
                </div>
                <div class="info-card">
                    <span>Experience</span>
                    <strong>Custom HTML sections with polished CSS styling</strong>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def section_title(title: str) -> None:
    st.markdown(f'<div class="panel-title">{title}</div>', unsafe_allow_html=True)


def sentiment_badge(label: str) -> str:
    return f"{ICON_MAP.get(label, '•')} {label.upper()}"


def show_result_card(label: str, compound: float) -> None:
    color = COLOR_MAP.get(label, "#94a3b8")
    glow = GLOW_MAP.get(label, "rgba(148, 163, 184, 0.2)")
    icon = ICON_MAP.get(label, "•")

    st.markdown(
        f"""
        <div style="
            position: relative;
            overflow: hidden;
            min-height: 280px;
            padding: 2rem;
            border-radius: 26px;
            border: 1px solid {color};
            background:
                radial-gradient(circle at top center, {glow}, transparent 34%),
                linear-gradient(180deg, rgba(8, 14, 28, 0.96), rgba(11, 17, 32, 0.9));
            box-shadow: 0 22px 70px rgba(2, 8, 23, 0.38);
            text-align: center;
        ">
            <div style="
                width: 76px;
                height: 76px;
                margin: 0 auto 1.15rem;
                border-radius: 999px;
                display: grid;
                place-items: center;
                font-size: 2rem;
                font-weight: 800;
                color: #08111f;
                background: linear-gradient(135deg, {color}, #f8fafc);
                box-shadow: 0 0 40px {glow};
            ">{icon}</div>
            <div style="
                color: {color};
                font-size: 2.3rem;
                font-weight: 800;
                letter-spacing: 0.08em;
            ">{label.upper()}</div>
            <div style="
                margin-top: 0.75rem;
                color: #cbd5e1;
                font-size: 1rem;
            ">Compound score</div>
            <div style="
                margin-top: 0.25rem;
                color: #f8fafc;
                font-size: 2rem;
                font-weight: 700;
            ">{compound:.4f}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

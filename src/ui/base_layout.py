import streamlit as st


def style_background_home():
    st.markdown(
        """
        <style>
            .stApp {
                background:
                    radial-gradient(ellipse at 50% 0%, rgba(56, 189, 248, 0.14), transparent 44%),
                    #08111e;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_background_dashboard():
    st.markdown(
        """
        <style>
            .stApp {
                background:
                    radial-gradient(ellipse at 100% 0%, rgba(45, 212, 191, 0.10), transparent 36%),
                    #08111e;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_base_layout():
    st.markdown(
        """
        <style>
            :root {
                color-scheme: dark;
                --ink: #f1f5f9;
                --muted: #b6c2d0;
                --primary: #38bdf8;
                --primary-hover: #0ea5e9;
                --teal: #2dd4bf;
                --surface: #111c2e;
                --surface-raised: #17263a;
                --border: #293a50;
                --soft: #1a2b40;
                --shadow: 0 16px 40px rgba(0, 0, 0, 0.30);
            }

            html, body, [class*="css"] {
                font-family: Inter, ui-sans-serif, system-ui, -apple-system,
                    BlinkMacSystemFont, "Segoe UI", sans-serif;
                color: var(--ink);
            }

            .stApp {
                --text-color: var(--ink);
                --secondary-text-color: var(--muted);
                --primary-color: var(--primary);
                --background-color: #08111e;
                --secondary-background-color: var(--surface);
                --border-color: var(--border);
                color: var(--ink) !important;
                background-color: var(--background-color);
            }

            [data-testid="stAppViewContainer"],
            [data-testid="stMain"] {
                background: transparent;
            }

            #MainMenu, footer, [data-testid="stHeader"] {
                visibility: hidden;
            }

            .block-container {
                max-width: 1160px;
                padding: 2rem 2rem 3rem;
            }

            .stApp h1, .stApp h2, .stApp h3, .stApp h4 {
                color: var(--ink) !important;
                font-weight: 700;
                letter-spacing: -0.035em;
            }

            h1 {
                font-size: clamp(2rem, 4vw, 3rem) !important;
                line-height: 1.12 !important;
                margin-bottom: 0.4rem !important;
            }

            h2 {
                font-size: clamp(1.5rem, 3vw, 2rem) !important;
                line-height: 1.2 !important;
            }

            h3 {
                font-size: 1.25rem !important;
                line-height: 1.35 !important;
            }

            .stApp [data-testid="stMarkdownContainer"] {
                color: var(--ink) !important;
            }

            .stApp [data-testid="stMarkdownContainer"] p,
            .stApp [data-testid="stMarkdownContainer"] li,
            .stApp [data-testid="stMarkdownContainer"] blockquote,
            .stApp [data-testid="stMarkdownContainer"] code {
                color: var(--ink) !important;
            }

            .stApp [data-testid="stWidgetLabel"],
            .stApp [data-testid="stWidgetLabel"] *,
            .stApp [data-testid="stCheckbox"] label,
            .stApp [data-testid="stRadio"] label,
            .stApp [data-testid="stToggle"] label {
                color: var(--ink) !important;
            }

            .stApp [data-testid="stCaptionContainer"],
            .stApp [data-testid="stCaptionContainer"] * {
                color: var(--muted) !important;
            }

            .stApp [data-testid="stMetricLabel"],
            .stApp [data-testid="stMetricLabel"] *,
            .stApp [data-testid="stMetricValue"],
            .stApp [data-testid="stDataFrame"] * {
                color: var(--ink) !important;
            }

            .stApp input,
            .stApp textarea,
            .stApp [role="combobox"],
            .stApp [role="option"] {
                color: var(--ink) !important;
                -webkit-text-fill-color: var(--ink) !important;
            }

            .stApp input::placeholder,
            .stApp textarea::placeholder {
                color: var(--muted) !important;
                -webkit-text-fill-color: var(--muted) !important;
                opacity: 1;
            }

            [data-testid="stVerticalBlockBorderWrapper"] {
                background: var(--surface);
                border: 1px solid var(--border);
                border-radius: 22px;
                box-shadow: var(--shadow);
                padding: 1.25rem;
                transition: border-color 180ms ease, box-shadow 180ms ease,
                    transform 180ms ease;
            }

            [data-testid="stVerticalBlockBorderWrapper"]:hover {
                border-color: #3b82a0;
                box-shadow: 0 20px 46px rgba(0, 0, 0, 0.38);
                transform: translateY(-2px);
            }

            div.stButton > button {
                min-height: 2.8rem;
                border: 1px solid transparent;
                border-radius: 12px;
                font-weight: 600;
                transition: background-color 160ms ease, border-color 160ms ease,
                    box-shadow 160ms ease, transform 160ms ease;
            }

            div.stButton > button[kind="primary"] {
                background: var(--primary);
                color: #082f49 !important;
                box-shadow: 0 5px 16px rgba(56, 189, 248, 0.22);
            }

            div.stButton > button[kind="primary"]:hover {
                background: var(--primary-hover);
                border-color: var(--primary-hover);
                box-shadow: 0 8px 22px rgba(56, 189, 248, 0.30);
                transform: translateY(-1px);
            }

            div.stButton > button[kind="secondary"] {
                background: var(--surface-raised);
                color: var(--ink) !important;
                border-color: var(--border);
            }

            div.stButton > button[kind="secondary"]:hover {
                background: var(--soft);
                border-color: #49627c;
            }

            div.stButton > button[kind="tertiary"] {
                background: #351a24;
                color: #fecaca !important;
                border-color: #713044;
            }

            div.stButton > button[kind="tertiary"]:hover {
                background: #4a1d2b;
                border-color: #9f3b55;
            }

            div.stButton > button:focus-visible {
                outline: 3px solid rgba(56, 189, 248, 0.55);
                outline-offset: 2px;
            }

            div[data-baseweb="input"] > div,
            div[data-baseweb="select"] > div,
            textarea {
                background: #0d1726;
                border-color: var(--border);
                border-radius: 11px;
            }

            [data-baseweb="popover"],
            [role="listbox"],
            [role="option"] {
                background-color: var(--surface-raised);
                color: var(--ink);
            }

            div[data-baseweb="input"] > div:focus-within,
            div[data-baseweb="select"] > div:focus-within,
            textarea:focus {
                border-color: var(--primary);
                box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.20);
            }

            [data-testid="stFileUploader"],
            [data-testid="stCameraInput"],
            [data-testid="stAudioInput"] {
                border-radius: 16px;
            }

            [data-testid="stAlert"] {
                border-radius: 14px;
            }

            hr {
                border-color: var(--border);
            }

            .brand-lockup {
                display: flex;
                align-items: center;
                gap: 0.9rem;
            }

            .brand-lockup img {
                width: 64px;
                height: 64px;
                object-fit: contain;
            }

            .brand-lockup h1,
            .brand-lockup h2 {
                margin: 0 !important;
                color: var(--ink);
                letter-spacing: -0.045em;
            }

            .brand-lockup p {
                margin: 0.2rem 0 0;
                font-size: 0.9rem;
            }

            .brand-lockup-home {
                justify-content: center;
                text-align: left;
                margin: 1rem 0 2.5rem;
            }

            .brand-lockup-home img {
                width: 84px;
                height: 84px;
            }

            .brand-lockup-home h1 {
                font-size: 2.8rem !important;
            }

            .brand-lockup-dashboard h2 {
                font-size: 1.6rem !important;
            }

            .subject-card {
                background: var(--surface);
                border: 1px solid var(--border);
                border-left: 5px solid var(--primary);
                border-radius: 18px;
                padding: 1.25rem;
                margin-bottom: 0.8rem;
                box-shadow: 0 8px 24px rgba(0, 0, 0, 0.22);
            }

            .subject-card h3 {
                margin: 0;
                color: var(--ink);
            }

            .subject-card p {
                margin: 0.65rem 0 0.9rem;
                font-size: 0.94rem;
            }

            .subject-code {
                display: inline-block;
                padding: 0.2rem 0.55rem;
                border-radius: 7px;
                background: #0b2a3a;
                color: #7dd3fc;
                font-weight: 650;
            }

            .subject-stats {
                display: flex;
                gap: 0.5rem;
                flex-wrap: wrap;
            }

            .subject-stat {
                padding: 0.4rem 0.7rem;
                border: 1px solid #34445a;
                border-radius: 10px;
                background: #18283b;
                color: #d7e2ee;
                font-size: 0.88rem;
            }

            .footer-credit {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 0.5rem;
                margin-top: 2.5rem;
                color: var(--muted);
                font-size: 0.85rem;
            }

            .footer-credit p {
                margin: 0;
                color: inherit;
            }

            .footer-credit img {
                max-height: 22px;
                object-fit: contain;
            }

            @media (max-width: 640px) {
                .block-container {
                    padding: 1.2rem 1rem 2rem;
                }

                [data-testid="stVerticalBlockBorderWrapper"] {
                    border-radius: 17px;
                    padding: 1rem;
                }

                .brand-lockup-home {
                    margin: 0.5rem 0 1.5rem;
                }

                .brand-lockup-home img {
                    width: 64px;
                    height: 64px;
                }

                .brand-lockup-home h1 {
                    font-size: 2.1rem !important;
                }
            }

            @media (prefers-reduced-motion: reduce) {
                *, *::before, *::after {
                    scroll-behavior: auto !important;
                    transition-duration: 0.01ms !important;
                    animation-duration: 0.01ms !important;
                }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

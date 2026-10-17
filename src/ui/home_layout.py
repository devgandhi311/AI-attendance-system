import streamlit as st

# ---------- Inline SVG icons (no external files needed) ----------
LOGO_SVG = """<svg class="logo" viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
<defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="#2dd4bf"/><stop offset="1" stop-color="#60a5fa"/></linearGradient></defs>
<circle cx="32" cy="32" r="30" fill="#ffffff" fill-opacity="0.08" stroke="url(#lg)" stroke-width="2"/>
<path d="M32 14 L54 25 L32 36 L10 25 Z" fill="url(#lg)"/>
<path d="M18 31 V41 C18 45 25 49 32 49 C39 49 46 45 46 41 V31 L32 38 Z" fill="#ffffff" fill-opacity="0.92"/>
<circle cx="47" cy="45" r="9" fill="#10b981"/>
<path d="M42.5 45 L46 48.5 L51.5 42" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""

TEACHER_SVG = """<svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg">
<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/><circle cx="12" cy="9" r="1.8"/><path d="M8.5 13c.6-1.6 2-2.3 3.5-2.3s2.9.7 3.5 2.3"/></svg>"""

STUDENT_SVG = """<svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg">
<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11.5V16c0 1.5 2.7 3 6 3s6-1.5 6-3v-4.5"/><path d="M22 9v6"/></svg>"""


def style_home_layout():
    """Inject the global CSS for the home page (responsive)."""
    st.markdown(
        """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

/* ---------- Page ---------- */
html, body, [class*="css"], .stApp {
    font-family: 'Poppins', 'Segoe UI', Arial, sans-serif;
}
.stApp {
    background: radial-gradient(circle at 12% 8%, #1d4ed8 0%, rgba(29,78,216,0) 42%),
                radial-gradient(circle at 88% 92%, #0f766e 0%, rgba(15,118,110,0) 42%),
                linear-gradient(160deg, #0b1730 0%, #0c2347 100%);
    background-attachment: fixed;
}
#MainMenu, footer, header[data-testid="stHeader"] { visibility: hidden; height: 0; }
.block-container {
    padding: 1.5rem 1rem 2rem 1rem;
    max-width: 1050px;
}

/* ---------- Header banner ---------- */
.hero {
    display: flex; flex-wrap: wrap; align-items: center; justify-content: center;
    gap: clamp(12px, 3vw, 24px);
    padding: clamp(22px, 4vw, 38px) clamp(16px, 3vw, 30px);
    border-radius: 22px;
    background: rgba(255, 255, 255, 0.07);
    border: 1px solid rgba(255, 255, 255, 0.18);
    backdrop-filter: blur(8px);
    box-shadow: 0 18px 40px rgba(0, 0, 0, 0.35);
    text-align: left;
}
.hero .logo { width: clamp(52px, 9vw, 72px); height: clamp(52px, 9vw, 72px); flex-shrink: 0; }
.hero-text h1 {
    margin: 0; font-weight: 700; letter-spacing: 0.5px; line-height: 1.15;
    font-size: clamp(1.6rem, 5vw, 2.7rem);
    background: linear-gradient(90deg, #ffffff 0%, #99f6e4 50%, #93c5fd 100%);
    -webkit-background-clip: text; background-clip: text; color: transparent;
}
.hero-text p {
    margin: 6px 0 0 0; color: #cbd5e1; font-weight: 400;
    font-size: clamp(0.85rem, 2.4vw, 1.05rem);
}

.section-title {
    text-align: center; color: #e2e8f0; font-weight: 600;
    font-size: clamp(1.05rem, 3vw, 1.4rem);
    margin: clamp(22px, 4vw, 34px) 0 clamp(16px, 3vw, 24px) 0;
}
.section-title span { color: #5eead4; }

/* ---------- Responsive columns: stack when narrow ---------- */
[data-testid="stHorizontalBlock"] { flex-wrap: wrap; row-gap: 1.5rem; }
[data-testid="stColumn"] { min-width: min(300px, 100%); }

/* ---------- Cards (st.container with key) ---------- */
.st-key-teacher_card, .st-key-student_card {
    border-radius: 20px;
    padding: 0 0 26px 0;
    background: #ffffff;
    box-shadow: 0 14px 34px rgba(0, 0, 0, 0.35);
    transition: transform .25s ease, box-shadow .25s ease;
    overflow: hidden;
}
.st-key-teacher_card:hover, .st-key-student_card:hover {
    transform: translateY(-6px);
    box-shadow: 0 22px 44px rgba(0, 0, 0, 0.5);
}

.card-top {
    display: flex; flex-direction: column; align-items: center;
    padding: clamp(22px, 4vw, 32px) 20px clamp(16px, 3vw, 24px) 20px;
    margin-bottom: 18px; color: #fff;
}
.card-top.teacher { background: linear-gradient(135deg, #1d4ed8, #2563eb); }
.card-top.student { background: linear-gradient(135deg, #0d9488, #14b8a6); }
.card-top h2 {
    margin: 12px 0 0 0; font-weight: 600; color: #fff;
    font-size: clamp(1.3rem, 3.5vw, 1.65rem);
}
.card-icon { width: clamp(46px, 8vw, 58px); height: clamp(46px, 8vw, 58px); }

.card-desc {
    text-align: center; color: #475569; line-height: 1.6;
    font-size: clamp(0.88rem, 2.2vw, 0.98rem);
    padding: 0 clamp(16px, 3vw, 26px); margin-bottom: 6px;
}
@media (min-width: 700px) { .card-desc { min-height: 78px; } }

/* ---------- Centered buttons inside cards ---------- */
.st-key-teacher_card .stButton, .st-key-student_card .stButton {
    display: flex; justify-content: center; padding: 0 16px;
}
.st-key-teacher_card .stButton > button,
.st-key-student_card .stButton > button {
    min-width: min(240px, 100%); width: auto;
    border: none; border-radius: 999px;
    padding: 12px 34px; font-size: 1.05rem; font-weight: 600; color: #ffffff;
    box-shadow: 0 8px 18px rgba(0, 0, 0, 0.22);
    transition: filter .2s ease, transform .1s ease, box-shadow .2s ease;
}
.st-key-teacher_card .stButton > button { background: linear-gradient(135deg, #1d4ed8, #2563eb); }
.st-key-student_card .stButton > button { background: linear-gradient(135deg, #0d9488, #14b8a6); }
.st-key-teacher_card .stButton > button:hover,
.st-key-student_card .stButton > button:hover {
    filter: brightness(1.12); color: #fff; box-shadow: 0 12px 24px rgba(0, 0, 0, 0.3);
}
.st-key-teacher_card .stButton > button:active,
.st-key-student_card .stButton > button:active { transform: scale(0.97); }

.footer-note {
    text-align: center; color: #94a3b8; margin-top: 36px;
    font-size: clamp(0.72rem, 2vw, 0.85rem);
}

/* ---------- Small phones ---------- */
@media (max-width: 480px) {
    .hero { flex-direction: column; text-align: center; }
    .block-container { padding: 1rem 0.75rem 1.5rem 0.75rem; }
}
</style>
        """,
        unsafe_allow_html=True,
    )


def render_header():
    """Top banner: logo + 'Smart Class Attendance'."""
    st.markdown(
        f"""<div class="hero">{LOGO_SVG}<div class="hero-text"><h1>Smart Class Attendance</h1><p>AI-powered face recognition attendance system</p></div></div>
<div class="section-title">Welcome! Please choose how you want to <span>continue</span></div>""",
        unsafe_allow_html=True,
    )


def render_card_top(role: str):
    """Coloured top part of a role card. role = 'teacher' | 'student'."""
    if role == "teacher":
        icon, title = TEACHER_SVG, "Teacher"
        desc = "Create classes, take attendance with face recognition and view reports."
    else:
        icon, title = STUDENT_SVG, "Student"
        desc = "Check your attendance, mark presence and track your records."
    st.markdown(
        f"""<div class="card-top {role}">{icon}<h2>{title}</h2></div><div class="card-desc">{desc}</div>""",
        unsafe_allow_html=True,
    )


def render_footer():
    st.markdown(
        '<div class="footer-note">© Smart Class Attendance · Powered by DEV SHREY</div>',
        unsafe_allow_html=True,
    )
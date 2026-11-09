
import streamlit as st


def style_teacher_layout():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&display=swap');

    .stApp {
        background: #e2e3ff;
        font-family: 'Poppins', sans-serif;
    }

    #MainMenu, footer, header[data-testid="stHeader"] {
        visibility: hidden;
    }

    .block-container {
        max-width: 1150px;
        padding: 1.5rem 2rem 2rem 2rem;
    }

    /* Header */
    .teacher-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 15px;
        margin-bottom: 30px;
    }

    .brand {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .brand-icon {
        width: 65px;
        height: 65px;
        border-radius: 16px;
        background: #ffe600;
        border: 2px solid #111;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 35px;
    }

    .brand-name {
        font-size: 32px;
        font-weight: 900;
        line-height: 0.85;
        color: #5865e8;
        letter-spacing: -1.5px;
    }

    .dashboard-title {
        font-size: clamp(27px, 4vw, 40px);
        font-weight: 900;
        color: #080808;
        margin: 12px 0 5px 0;
        letter-spacing: -1px;
    }

    .dashboard-subtitle {
        color: #626477;
        font-size: 14px;
        margin-bottom: 28px;
    }

    /* Dashboard cards */
    .stat-card {
        background: #ffffff;
        padding: 23px;
        border-radius: 18px;
        box-shadow: 0 6px 18px rgba(70, 70, 130, 0.10);
        border: 1px solid rgba(255,255,255,.8);
        min-height: 135px;
    }

    .stat-label {
        color: #77798d;
        font-size: 14px;
        font-weight: 500;
    }

    .stat-value {
        color: #171717;
        font-size: 32px;
        font-weight: 800;
        margin-top: 8px;
    }

    .stat-icon {
        font-size: 25px;
    }

    .section-heading {
        color: #101010;
        font-size: 21px;
        font-weight: 800;
        margin: 30px 0 15px 0;
    }

    .action-card {
        background: #fff;
        padding: 22px;
        border-radius: 18px;
        min-height: 145px;
        box-shadow: 0 6px 18px rgba(70,70,130,.10);
    }

    .action-icon {
        font-size: 30px;
        margin-bottom: 10px;
    }

    .action-title {
        color: #171717;
        font-size: 17px;
        font-weight: 700;
    }

    .action-desc {
        color: #77798d;
        font-size: 12px;
        margin-top: 5px;
    }

    /* Buttons */
    .stButton > button {
        border: none !important;
        border-radius: 50px !important;
        font-family: 'Poppins', sans-serif !important;
        font-weight: 600 !important;
        min-height: 45px;
        transition: all .2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        filter: brightness(1.05);
    }

    /* Main dashboard buttons */
    .st-key-create_class button,
    .st-key-take_attendance button {
        background: #5865ed !important;
        color: white !important;
    }

    .st-key-manage_students button,
    .st-key-view_reports button {
        background: #e83d9b !important;
        color: white !important;
    }

    .st-key-back_home button {
        background: #e83d9b !important;
        color: white !important;
    }

    .footer-text {
        text-align: center;
        color: #77798d;
        font-size: 12px;
        margin-top: 45px;
        padding-bottom: 10px;
    }

    @media(max-width: 600px) {
        .block-container {
            padding: 1rem;
        }
        .brand-name {
            font-size: 25px;
        }
        .brand-icon {
            width: 55px;
            height: 55px;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def render_teacher_header():
    st.markdown("""
    <div class="teacher-header">
        <div class="brand">
            <div class="brand-icon">🎓</div>
            <div class="brand-name">SNAP<br>CLASS</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_teacher_footer():
    st.markdown("""
    <div class="footer-text">
        Created with ❤️ by Me
    </div>
    """, unsafe_allow_html=True)


def render_stat_card(icon, label, value):
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-icon">{icon}</div>
        <div class="stat-label">{label}</div>
        <div class="stat-value">{value}</div>
    </div>
    """, unsafe_allow_html=True)


def render_action_card(icon, title, description):
    st.markdown(f"""
    <div class="action-card">
        <div class="action-icon">{icon}</div>
        <div class="action-title">{title}</div>
        <div class="action-desc">{description}</div>
    </div>
    """, unsafe_allow_html=True)

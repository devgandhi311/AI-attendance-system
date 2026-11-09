import streamlit as st
from ui.home_layout import (
    style_home_layout,
    render_header,
    render_card_top,
    render_footer,
)
from src.components.header import header

def home():
    header()
    style_home_layout()
    render_header()

    col1, col2 = st.columns(2, gap="large")

    with col1:
        with st.container(key="student_card"):
            render_card_top("student")

            left, center, right = st.columns([1, 2, 1])

            with left:
                if st.button("Login as Student", key="btn_student", use_container_width=True):
                    st.session_state["login_type"] = "student"
                    st.rerun()

    with col2:
        with st.container(key="teacher_card"):
            render_card_top("teacher")

            left, center, right = st.columns([1, 2, 1])

            with left:
                if st.button("Login as Teacher", key="btn_teacher", use_container_width=True):
                    st.session_state["login_type"] = "teacher"
                    st.rerun()

    render_footer()
import streamlit as st

from src.components.footer import footer_home
from src.components.header import header_home
from src.ui.base_layout import style_background_home, style_base_layout


def home_screen():

    header_home()
    style_background_home()
    style_base_layout()

    st.markdown(
        "<p style='text-align:center; margin:-1.5rem 0 2rem;'>"
        "Choose your portal to get started</p>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        with st.container(border=True):
            st.header("Student")
            st.caption("Check in with Face ID and keep track of your classes.")
            st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=120)
            if st.button(
                "Open Student Portal",
                type="primary",
                icon=":material/arrow_outward:",
                icon_position="right",
                width="stretch",
            ):
                st.session_state["login_type"] = "student"
                st.rerun()

    with col2:
        with st.container(border=True):
            st.header("Teacher")
            st.caption("Manage classes and take attendance with AI.")
            st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=145)
            if st.button(
                "Open Teacher Portal",
                type="primary",
                icon=":material/arrow_outward:",
                icon_position="right",
                width="stretch",
            ):
                st.session_state["login_type"] = "teacher"
                st.rerun()

    footer_home()

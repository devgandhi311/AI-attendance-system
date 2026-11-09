import streamlit as st
import re
from src.ui.login_layout import login_layout
from src.database.db import teacher_login



def login():

    login_layout()

    with st.form("login_form"):

        username = st.text_input(
            "Username",
            placeholder="Enter your username"
        )

        password = st.text_input(
            "Password",
            placeholder="Enter your password",
            type="password"
        )

        st.write("")

        submitted = st.form_submit_button(
            "Login",
            use_container_width=True
        )

        if submitted:

            if not username  or not password:
                st.error("Please fill in all fields.")

            else:
                st.success("Login details submitted successfully!")

                if teacher_login(username, password):
                    st.toast("Welcome back.")
                    import time
                    time.sleep(2)
                    st.session_state["isLogin"] = True
                    st.rerun()
                else:
                    st.error("Invalid username or password")

                # Add database authentication here.
                # Do not authenticate using form validation alone.

    st.markdown(
        "<p style='text-align:center;color:#666;'>"
        "Don't have an account?</p>",
        unsafe_allow_html=True
    )
    left, center, right = st.columns([3, 4, 1])

    with center:
        if st.button("Create New Account"):
            st.session_state["page"] = "register"
            st.rerun()



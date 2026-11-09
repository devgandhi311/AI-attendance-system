import streamlit as st
import re
from src.ui.signup_layout import signup_layout

def signup():

    signup_layout()    

    with st.form("signup_form"):

        username = st.text_input(
            "Username",
            placeholder="Choose a username"
        )

        email = st.text_input(
            "Email Address",
            placeholder="Enter your email address"
        )

        password = st.text_input(
            "Password",
            placeholder="Create a password",
            type="password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            placeholder="Re-enter your password",
            type="password"
        )

        st.write("")

        submitted = st.form_submit_button(
            "Create Account",
            use_container_width=True
        )

        if submitted:

            if not all([
                username.strip(),
                email.strip(),
                password,
                confirm_password
            ]):
                st.error("Please fill in all fields.")

            elif not re.fullmatch(
                r"[^@\s]+@[^@\s]+\.[^@\s]+", email
            ):
                st.error("Please enter a valid email address.")

            elif len(password) < 8:
                st.error("Password must contain at least 8 characters.")

            elif password != confirm_password:
                st.error("Passwords do not match.")

            else:
                # Connect database registration here.
                st.success("All details are valid! Account registration can proceed.")
                st.session_state["isLogin"] = True

    st.markdown(
        "<p style='text-align:center;color:#cbd5e1;'>"
        "Already have an account?</p>",
        unsafe_allow_html=True
    )

    left, center, right = st.columns([3, 4, 1])
    
    with center:
        if st.button("Login Instead"):
            st.session_state["page"] = "login"
            st.rerun()

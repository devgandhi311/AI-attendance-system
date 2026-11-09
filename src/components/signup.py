import streamlit as st
import re
from src.ui.signup_layout import signup_layout
from src.database.db import check_teacher_exists, create_teacher

def register_teacher(username, name, pwd, confirm_pass):
    if not username or not name or not pwd or not confirm_pass:
        return False, "All fields are required"
    if pwd!=confirm_pass:
        return False, "Password does not match"
    if check_teacher_exists(username):
        return False, "username already taken"

    try:
        create_teacher(username=username, name=name, password=pwd)
        return True, "Sucessfully Created."
    except Exception as e:
        return False, st.exception(e)
    
def signup():
    signup_layout()    

    with st.form("signup_form"):

        username = st.text_input(
            "Username",
            placeholder="Choose a username"
        )

        name = st.text_input(
            "name",
            placeholder="Enter your name"
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
                password,
                confirm_password
            ]):
                st.error("Please fill in all fields.")


            elif password != confirm_password:
                st.error("Passwords do not match.")

            else:
                # Connect database registration here.
                # st.success("All details are valid! Account registration can proceed.")
                success, message = register_teacher(username=username,name=name, pwd=password, confirm_pass=confirm_password)
                if success:
                    st.success(message)
                    import time
                    time.sleep(2)
                    st.session_state["teacher_data"] = {"name": name, "username": username, "password": password}
                    st.session_state["isLogin"] = True
                    st.rerun()
                else:
                    st.error(message)
                    

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

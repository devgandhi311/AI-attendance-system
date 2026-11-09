import streamlit as st
from src.components.signup import signup
from src.components.login import login

def teacher_dashboard():    
    # st.title("Teacher Dashboard")
    # st.write("Welcome to the teacher dashboard!")
    if st.session_state["isLogin"]!=True:
        if (st.session_state["page"]!="register"):
            login()
        elif (st.session_state["page"]=="register"):
            signup()
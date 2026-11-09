import streamlit as st
from src.components.signup import signup
from src.components.login import login
from src.components.header import header

def teacher_dashboard():    
    header()
    if st.session_state["isLogin"]!=True:
        if (st.session_state["page"]!="register"):
            login()
        elif (st.session_state["page"]=="register"):
            signup()
    else:
        st.title("Teacher Dashboard")
        st.write(f"Welcome {st.session_state['teacher_data'].get('username')}")

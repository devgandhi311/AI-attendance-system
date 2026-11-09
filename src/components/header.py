import streamlit as st

def header():
    st.header("AI Attendance System")
    st.write("Welcome to the AI Attendance System!")  

    if st.button("Go Home"):
        st.session_state["login_type"]=None
        st.rerun()  
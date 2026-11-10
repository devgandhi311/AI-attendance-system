import streamlit as st
from src.screens.teacher_dashboard import teacher_dashboard
from src.screens.student_dashboard import student_dashboard
from src.screens.home import home



def main():
    if "student_data" not in st.session_state:
        st.session_state["student_data"] = None
    if "teacher_data" not in st.session_state:
        st.session_state["teacher_data"] = None
    if "login_type" not in st.session_state:
        st.session_state["login_type"] = None
    if "page" not in st.session_state:
        st.session_state["page"] = None
    if "isLogin" not in st.session_state:
        st.session_state["isLogin"] = None    
    if "sLogin" not in st.session_state:
        st.session_state["sLogin"] = None

    match st.session_state["login_type"]:
        case "teacher":
            teacher_dashboard()
        case "student": 
            student_dashboard()     
        case None:
            home()

main()
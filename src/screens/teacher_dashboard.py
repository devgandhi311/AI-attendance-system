import streamlit as st
from src.components.signup import signup
from src.components.login import login
from src.components.header import header
from src.components.dialog_create_subject import create_subject_dialog
from src.database.db import get_teacher_subjects
def teacher_dashboard():    
    header()
    if st.session_state["isLogin"]!=True:
        if (st.session_state["page"]!="register"):
            login()
        elif (st.session_state["page"]=="register"):
            signup()
    else:
        st.title("Teacher Dashboard")
        st.subheader(f"Welcome {st.session_state['teacher_data'].get('username')}")

        if st.button("Logout", type="secondary", key="logoutbtn"):
            st.session_state["isLogin"]=False
            del st.session_state.teacher_data
            st.rerun()

        st.space()

        if "current_teacher_tab" not in st.session_state:
            st.session_state["current_teacher_tab"]="take_attendance"
        tab1, tab2, tab3 = st.columns(3)

        with tab1:
            type1 = "primary" if st.session_state["current_teacher_tab"] == "take_attendance" else "tertiary"
            if st.button("Take Attendance", width="stretch", key="tab1", type=type1):
                st.session_state["current_teacher_tab"] = "take_attendance"
                st.rerun()

        with tab2:
            type2 = "primary" if st.session_state["current_teacher_tab"] == "manage_subjects" else "tertiary"
            if st.button("manage subjects", width="stretch", key="tab2", type=type2):
                st.session_state["current_teacher_tab"] = "manage_subjects"
                st.rerun()
                        
        with tab3:
            type3 = "primary" if st.session_state["current_teacher_tab"] == "attendance_records" else "tertiary"
            if st.button("attendance records", width="stretch", key="tab3", type=type3):
                st.session_state["current_teacher_tab"] = "attendance_records"
                st.rerun()

        st.divider()

        if st.session_state["current_teacher_tab"]=="take_attendance":
            teacher_tab_take_attendance()
        if st.session_state["current_teacher_tab"]=="manage_subjects":
            teacher_tab_manage_subjects()
        if st.session_state["current_teacher_tab"]=="attendance_records":
            teacher_tab_attendance_records()


def teacher_tab_take_attendance():
    st.header("Take Ai attendance")

def teacher_tab_manage_subjects():
    teacher_id = st.session_state["teacher_data"].get("teacher_id")
    if teacher_id is None or teacher_id == "null":
        st.error("Teacher ID not found. Please log in again.")
        st.stop()
    col1, col2 = st.columns(2)

    with col1:
        st.header("Manage subjects", width="stretch")
    with col2:
        if st.button("Create new subject", width="stretch"):
            create_subject_dialog(teacher_id)

    subjects = get_teacher_subjects(teacher_id)
    if subjects:
        for sub in subjects:
            stats = [
                ("Students", sub["total_students"]),
                ("Classes", sub["total_classes"])
            ]

        def share_btn():
            if st.button(f"Share Code: {sub["name"]}", key=f"share_{sub["subject_code"]}"):
                share_subject_dialog(sub["name"], sub["subjject_code"])

            st.space()

        subject_card(
            name = sub["name"],
            code = sub["subject_code"],
            section = sub["section"],
            stats = stats,
            footer_callback=share_btn
        )
    else:
        st.info("No subjects found, create one above")
    




def teacher_tab_attendance_records():
    st.header("Attendance records")
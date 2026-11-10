import streamlit as st
import numpy as np
from PIL import Image
from src.components.header import header
from src.piplines.face_pipline import predict_attendance, get_face_embeddings, train_classifier
from src.database.db import get_all_students, create_student
from src.piplines.voice_pipline import get_voice_embedding 

def student_dashboard():
    show_registration=False
    header()
    if (st.session_state["sLogin"] != True):
        photo_source = st.camera_input("Center your face")
    
        if (photo_source):
            img = np.array(Image.open(photo_source))

            with st.spinner("AI is scanning..."):
                detected, all_ids, num_faces = predict_attendance(img)

                if num_faces==0:
                    st.warning("Face not found.")
                elif num_faces>1:
                    st.warning("Multiple Faces found")
                else:
                    if detected:
                        student_id = list(detected.keys())[0]
                        all_students = get_all_students()

                        student = ((s for s in all_students if s["student_id"]==student_id), None)

                        if student:
                            st.session_state["student_data"] = student
                            st.session_state["sLogin"] = True
                            st.toast(f"welcome back {student['name']}")
                            import time
                            time.sleep(2)
                            st.rerun()
                    else:
                        st.info("Face not recognized! You might be a new student.")
                        show_registration=True
    elif show_registration:
        with st.container(border=True):
            st.header("register new profile")
            new_name = st.text_input("Enter your name", placeholder='E.g Shrey Marakana')

            st.subheader("optional: voice enrillment")
            st.info("Enroll your for voice only attendance")


            audi_data=None

            try:
                audio_data=st.audio_input("Record a short phrase like I am present, My name is shrey yes sir yes madam.")
            except Exception as e:
                st.error("Audio data failed!")

            if st.button("Create Account", type="primary"):
                if new_name:
                    with st.spinner("Creating profile..."):
                        img = np.array(Image.open(photo_source))

                        encodings = get_face_embeddings(img)

                        if encodings:
                            face_emb = encodings[0].tolist()

                            voice_emb=None
                            if audio_data:
                                voice_emb = get_voice_embedding(audio_data.read())

                            response_data = create_student(new_name, face_emb, voice_emb)

                            if response_data:
                                train_classifier()
                                st.session_state["student_data"] = response_data[0]
                                st.session_state["sLogin"] = True
                                st.toast(f"Profile created!  {new_name}")

                                time.sleep(2)
                                st.rerun()
                        else:
                            st.error("could not capture your facial features for registration")

                else:
                    st.warning("please enter your name")
    else:
        st.title("Student Dashboard")
        st.write("Welcome to the student dashboard!")

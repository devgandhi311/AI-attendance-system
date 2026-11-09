import streamlit as st
import numpy as np
from PIL import Image
from src.components.header import header

def student_dashboard():
    header()
    if (st.session_state["sLogin"] != True):
        photo_source = st.camera_input("Center your face")
    
        if (photo_source):
            np.array(Image.open(photo_source))

    else:
        st.title("Student Dashboard")
        st.write("Welcome to the student dashboard!")
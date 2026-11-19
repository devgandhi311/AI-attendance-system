import streamlit as st


def footer_home():
    logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"

    st.markdown(
        f"""
        <div class="footer-credit">
        <p>Made with ❤️ by</p>
        <img src="{logo_url}" alt="Apna College" />
        </div>
        """,
        unsafe_allow_html=True,
    )


def footer_dashboard():
    logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"

    st.markdown(
        f"""
        <div class="footer-credit">
        <p>Made with ❤️ by Me</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

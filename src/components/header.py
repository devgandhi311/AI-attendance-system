import streamlit as st


def header_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(
        f"""
        <div class="brand-lockup brand-lockup-home">
            <img src="{logo_url}" alt="SnapClass logo" />
            <div>
                <h1>SnapClass</h1>
                <p>AI-powered attendance, made simple</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def header_dashboard():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(
        f"""
        <div class="brand-lockup brand-lockup-dashboard">
            <img src="{logo_url}" alt="SnapClass logo" />
            <h2>SnapClass</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

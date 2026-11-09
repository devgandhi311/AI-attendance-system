import streamlit as st

def login_layout():
    st.markdown("""
        
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&display=swap');
    
        .stApp {
            background: linear-gradient(135deg, #101827, #172554);
            font-family: 'Poppins', sans-serif;
        }
    
        .block-container {
            max-width: 650px;
            padding-top: 3rem;
        }
    
        .login-title {
            text-align: center;
            font-size: 38px;
            font-weight: 900;
            color: #ffffff;
            margin-bottom: 8px;
        }
    
        .login-subtitle {
            text-align: center;
            color: #94a3b8;
            margin-bottom: 35px;
        }
    
        h1 {
            color: #38bdf8 !important;
        }
    
        label, .stTextInput label {
            color: #e2e8f0 !important;
            font-weight: 500 !important;
        }
    
        .stTextInput input {
            # background: #f1f5f9 !important;
            color: #ffffff !important;
            border: 1px solid #cbd5e1 !important;
            border-radius: 10px !important;
        }
    
        .stTextInput input:focus {
            border: 2px solid #38bdf8 !important;
            box-shadow: 0 0 8px rgba(56,189,248,.25) !important;
        }
    
        .stButton > button,
        .stFormSubmitButton > button {
            background: linear-gradient(90deg, #2563eb, #06b6d4) !important;
            color: white !important;
            border: none !important;
            border-radius: 30px !important;
            height: 48px;
            font-weight: 600;
            width: 100%;
            transition: all .2s ease;
        }
    
        .stButton > button:hover,
        .stFormSubmitButton > button:hover {
            filter: brightness(1.15);
            transform: translateY(-2px);
            color: white !important;
        }
    
        [data-testid="stForm"] {
            background: #1e293b;
            padding: 25px;
            border-radius: 18px;
            border: 1px solid #334155;
            box-shadow: 0 12px 35px rgba(0,0,0,.25);
        }
    
        .stMarkdown p {
            color: #cbd5e1;
        }
        </style>""", 
        unsafe_allow_html=True)
    
    # Logo
    st.markdown("""
        <h1 style="text-align:center;color:#5865ed;
        font-weight:900;line-height:1;">
        🎓 SNAP CLASS
        </h1>
        """, unsafe_allow_html=True)
    
    st.markdown(
            '<div class="login-title">Welcome Back!</div>',
            unsafe_allow_html=True
        )
    
    st.markdown(
            '<div class="login-subtitle">Login to your account</div>',
            unsafe_allow_html=True
        )
    
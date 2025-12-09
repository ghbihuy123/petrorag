import streamlit as st

def local_css(css: str):
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

sidebar_css = local_css("""
/* Strong & Stable Sidebar Override */
section[data-testid="stSidebar"] > div:first-child {
    background-color: #F37021 !important;
    padding: 20px !important;
}

/* Text inside sidebar */
section[data-testid="stSidebar"] * {
    color: #2F5FA9 !important;
}

/* Buttons */
section[data-testid="stSidebar"] button {
    background-color: rgba(255,255,255,0.15) !important;
    color: white !important;
    border-radius: 6px !important;
    border: 1px solid rgba(255,255,255,0.25) !important;
}

section[data-testid="stSidebar"] button:hover {
    background-color: rgba(255,255,255,0.25) !important;
}
""")


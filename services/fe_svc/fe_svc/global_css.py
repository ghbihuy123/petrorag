import streamlit as st

def local_css(css: str):
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

sidebar_css = local_css("""
/* Sidebar container */
[data-testid="stSidebar"] {
    background-color: #F37021 !important;  /* Petrolimex Orange */
    padding: 20px !important;
}

/* Sidebar text color */
[data-testid="stSidebar"] * {
    color: #2F5FA9 !important;
}

/* Buttons inside sidebar */
[data-testid="stSidebar"] button {
    background-color: rgba(255,255,255,0.15) !important;
    color: white !important;
    border-radius: 6px !important;
    border: 1px solid rgba(255,255,255,0.25) !important;
}

/* Hover */
[data-testid="stSidebar"] button:hover {
    background-color: rgba(255,255,255,0.25) !important;
}

/* Divider color */
[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,0.3) !important;
}
                                                

"""
)


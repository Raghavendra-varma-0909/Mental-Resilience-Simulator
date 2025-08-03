import streamlit as st
from auth import login_user
from journal import journal_flow
from dashboard import show_dashboard

st.set_page_config(page_title="Resilience Journal", page_icon="🪞", layout="wide")

# --- Login / Session Management ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_user()
else:
    st.sidebar.title("Navigataion")
    choice = st.sidebar.radio("Go to:", ["Journal", "Dashboard"])

    if choice == "Journal":
        journal_flow()
    elif choice == "Dashboard":
        show_dashboard()
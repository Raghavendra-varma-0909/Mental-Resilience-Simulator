import streamlit as st

# Updated user credentials
USERS = {"ADMIN": "2005"}

def login_user():
    st.title("🔐 Login to Resilience Journal")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if USERS.get(username) == password:
            st.session_state.logged_in = True
            st.success("Login successful! Redirecting...")
            st.rerun()
        else:
            st.error("Invalid username or password")

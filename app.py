import streamlit as st
from auth import login, get_user_role

st.set_page_config(page_title="Project Tracker", layout="wide")

# User login
username = st.text_input("Username")
password = st.text_input("Password", type="password")
login_button = st.button("Login")

if login_button:
    role = login(username, password)
    if role:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.session_state.role = role
        st.success(f"Login successful as {role}")
    else:
        st.error("Invalid credentials")

# Restrict page visibility
if "logged_in" in st.session_state and st.session_state.logged_in:
    if st.session_state.role == "Student":
        st.switch_page("pages/1_Student_Portal.py")
    elif st.session_state.role == "Supervisor":
        st.switch_page("pages/2_Supervisor_Dashboard.py")

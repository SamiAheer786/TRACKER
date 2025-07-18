import streamlit as st
from auth import login
from student_portal import show_student_portal
from supervisor_portal import show_supervisor_portal  # If implemented

st.set_page_config(page_title="FYP Tracker", layout="centered")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None

if not st.session_state.logged_in:
    st.title("🔐 Login Portal")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        role = login(username, password)
        if role:
            st.session_state.logged_in = True
            st.session_state.role = role
            st.experimental_rerun()
        else:
            st.error("❌ Invalid credentials.")
else:
    st.sidebar.success(f"✅ Logged in as {st.session_state.role}")
    
    if st.session_state.role == "Student":
        show_student_portal()
    elif st.session_state.role == "Supervisor":
        show_supervisor_portal()

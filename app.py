import streamlit as st
from auth import login
from student_portal import show_student_portal
from supervisor_portal import show_supervisor_portal

# --- Session Initialization ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None

# --- Login Page ---
if not st.session_state.logged_in:
    st.title("Login Page")

    username = st.text_input("Username").strip()
    password = st.text_input("Password", type="password").strip()

    if st.button("Login"):
        role = login(username, password)
        if role:
            st.session_state.logged_in = True
            st.session_state.role = role
            st.success(f"Logged in as {role}")
        else:
            st.error("Invalid credentials")

# --- Role-based Redirection ---
if st.session_state.logged_in:
    st.sidebar.title("Menu")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.role = None
        st.experimental_rerun()  # Safe to rerun on logout

    if st.session_state.role == "Student":
        show_student_portal()
    elif st.session_state.role == "Supervisor":
        show_supervisor_portal()

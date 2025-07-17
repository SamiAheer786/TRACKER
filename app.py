# app.py

import streamlit as st
from auth import login, get_user_role

st.set_page_config(page_title="Final Year Project Tracker", layout="wide")

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.role = ""

if not st.session_state.logged_in:
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        role = login(username, password)
        if role:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.role = role
            st.success(f"Logged in as {role}")
            st.experimental_rerun()
        else:
            st.error("Invalid credentials")
else:
    st.sidebar.success(f"Welcome {st.session_state.username} ({st.session_state.role})")

    if st.session_state.role == "Student":
        st.switch_page("pages/1_Student_Portal.py")
    elif st.session_state.role == "Supervisor":
        st.switch_page("pages/2_Supervisor_Portal.py")

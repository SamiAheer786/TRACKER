import streamlit as st
from utils import add_or_update_project

st.header("👨‍👩‍👧 Group Submission Form")

with st.form("group_form"):
    group_id = st.text_input("Group ID")
    student_names = st.text_area("List all student names (comma-separated)")
    department = st.selectbox("Department", ["CS", "SE", "BBA", "EE"])
    title = st.text_input("Project Title")
    supervisor = st.text_input("Supervisor Name")
    progress = st.slider("Progress %", 0, 100)
    deadline = st.date_input("Deadline")
    submit = st.form_submit_button("Submit")

if submit:
    if group_id and student_names and title:
        add_or_update_project(group_id, student_names, department, title, supervisor, progress, deadline)
        st.success("Project details submitted.")
    else:
        st.warning("Please fill all required fields.")

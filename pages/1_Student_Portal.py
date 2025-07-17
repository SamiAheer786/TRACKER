import streamlit as st
import pandas as pd
from utils import save_uploaded_file, save_data, init_data_file

init_data_file()

st.title("📥 Student Project Submission Portal")

with st.form("submit_form"):
    name = st.text_input("Your Name")
    project_title = st.text_input("Project Title")
    supervisor = st.selectbox("Select Supervisor", ["Dr. Khan", "Ms. Ayesha", "Mr. Bilal"])
    progress = st.slider("Project Progress (%)", 0, 100, 25)
    file_upload = st.file_uploader("Upload Final Report", type=["pdf", "docx"])
    submit_btn = st.form_submit_button("Submit")

if submit_btn:
    if name and project_title and file_upload:
        file_path = save_uploaded_file(file_upload)
        save_data({
            "Name": name,
            "Project Title": project_title,
            "Supervisor": supervisor,
            "Progress": progress,
            "File": file_path
        })
        st.success("Project submitted successfully!")
    else:
        st.warning("Please fill all fields and upload a file.")

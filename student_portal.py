import streamlit as st
import pandas as pd
from utils import save_uploaded_file, append_submission, load_data

def show_student_portal():
    st.title("🎓 Student Submission Portal")

    reg_no = st.text_input("Registration Number")
    student_name = st.text_input("Student Name")
    project_title = st.text_input("Project Title")
    supervisor = st.text_input("Supervisor Name")
    uploaded_file = st.file_uploader("Upload Proposal (PDF)", type=["pdf"])

    if st.button("Submit"):
        if reg_no and student_name and project_title and supervisor and uploaded_file:
            file_path = save_uploaded_file(uploaded_file)
            data = {
                "RegNo": reg_no,
                "Name": student_name,
                "ProjectTitle": project_title,
                "Supervisor": supervisor,
                "File": file_path
            }
            append_submission(data)
            st.success("✅ Submission Successful!")
        else:
            st.error("❌ Please fill all fields and upload a file.")

    st.subheader("📜 Submission History")
    df = load_data()
    if not df.empty:
        filtered = df[df["RegNo"] == reg_no]
        st.dataframe(filtered)

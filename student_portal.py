import streamlit as st
from utils import save_uploaded_file, save_data, load_data

def show_student_portal():
    st.title("🎓 Student Portal")

    st.subheader("📋 Submit Your Project Information")
    
    with st.form("student_form"):
        name = st.text_input("Full Name")
        reg_no = st.text_input("Registration Number")
        project_title = st.text_input("Project Title")
        supervisor = st.text_input("Supervisor Name")
        uploaded_file = st.file_uploader("Upload Your Proposal (.pdf)", type=["pdf"])
        
        submitted = st.form_submit_button("Submit")

        if submitted:
            if not uploaded_file:
                st.error("⚠️ Please upload a file before submitting.")
            elif not name or not reg_no or not project_title or not supervisor:
                st.error("⚠️ Please fill out all the fields.")
            else:
                file_path = save_uploaded_file(uploaded_file)
                save_data({
                    "Name": name,
                    "RegNo": reg_no,
                    "ProjectTitle": project_title,
                    "Supervisor": supervisor,
                    "File": file_path
                })
                st.success("✅ Submission successful!")

    st.subheader("📄 Your Submission History")
    df = load_data()
    if not df.empty:
        st.dataframe(df)
    else:
        st.info("No submissions yet.")

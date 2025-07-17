import streamlit as st
from utils import save_uploaded_file, save_data, init_data_file

init_data_file()

if "role" not in st.session_state or st.session_state.role != "Student":
    st.warning("Access denied.")
    st.stop()

st.title("📚 Student Portal")

name = st.text_input("Your Name")
project = st.text_input("Project Name")
progress = st.slider("Progress (%)", 0, 100, 10)
supervisor = st.selectbox("Select Supervisor", ["supervisor1", "Other"])

if supervisor == "Other":
    supervisor = st.text_input("Enter Supervisor Name")

uploaded_file = st.file_uploader("Upload Project File", type=["pdf", "docx", "pptx"])

if st.button("Submit"):
    if name and project and uploaded_file:
        file_path = save_uploaded_file(uploaded_file)
        save_data({
            "Name": name,
            "Project": project,
            "Progress": progress,
            "Supervisor": supervisor,
            "File": file_path
        })
        st.success("Project submitted successfully!")
    else:
        st.error("Please fill all fields.")

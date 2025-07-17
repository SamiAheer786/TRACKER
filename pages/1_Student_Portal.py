import streamlit as st
from utils import save_uploaded_file, save_data, load_data

def show_student_portal():
    st.title("Student Portal")

    name = st.text_input("Enter Your Name")
    project = st.text_input("Project Title")
    progress = st.text_area("Progress Update")
    supervisor = st.selectbox("Select Supervisor", ["supervisor1", "Other"])

    if supervisor == "Other":
        supervisor = st.text_input("Enter Supervisor Name")

    uploaded_file = st.file_uploader("Upload your report")

    if st.button("Submit"):
        if uploaded_file:
            file_path = save_uploaded_file(uploaded_file)
        else:
            file_path = "No file uploaded"

        save_data({
            "Name": name,
            "Project": project,
            "Progress": progress,
            "Supervisor": supervisor,
            "File": file_path
        })

        st.success("Submitted Successfully!")

    st.markdown("---")
    st.subheader("Your Submission History")

    all_data = load_data()
    your_data = all_data[all_data["Name"] == name]

    if not your_data.empty:
        for _, row in your_data.iterrows():
            st.write(f"Project: {row['Project']}")
            st.write(f"Progress: {row['Progress']}")
            if row['File'] != "No file uploaded":
                st.markdown(f"[Download File]({row['File']})", unsafe_allow_html=True)
            st.markdown("---")
    else:
        st.info("No previous submissions found.")

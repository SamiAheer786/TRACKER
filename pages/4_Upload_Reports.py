import streamlit as st
from utils import save_uploaded_file

st.title("📁 Upload Final Reports")

uploaded_file = st.file_uploader("Choose your final report (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file is not None:
    file_path = save_uploaded_file(uploaded_file)
    st.success(f"File uploaded successfully: {file_path}")

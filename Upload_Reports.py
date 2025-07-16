import streamlit as st
import pandas as pd
from utils import load_data, save_data

st.header("📁 Upload Final Reports")

group_id = st.text_input("Group ID")
uploaded_file = st.file_uploader("Upload PDF/ZIP", type=["pdf", "zip"])

if st.button("Submit Report"):
    if group_id and uploaded_file:
        df = load_data()
        if group_id in df["Group ID"].values:
            # For simplicity, we'll just note file uploaded
            df.loc[df["Group ID"] == group_id, "Report Link"] = f"Uploaded: {uploaded_file.name}"
            save_data(df)
            st.success("Report uploaded and linked.")
        else:
            st.error("Group ID not found!")
    else:
        st.warning("Please provide Group ID and upload a file.")

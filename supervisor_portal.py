import streamlit as st
import pandas as pd
from utils import load_data

def show_supervisor_portal():
    st.title("Supervisor Dashboard")

    df = load_data()

    supervisor_name = st.text_input("Enter your name to view your assigned students")

    if supervisor_name:
        filtered_data = df[df['Supervisor'].str.lower() == supervisor_name.lower()]

        if filtered_data.empty:
            st.warning("No students assigned or submissions found.")
        else:
            st.success(f"Showing data for Supervisor: {supervisor_name}")
            for idx, row in filtered_data.iterrows():
                st.write(f"### Student Name: {row['Name']}")
                st.write(f"**Project Title:** {row['Project']}")
                st.write(f"**Progress Update:** {row['Progress']}")

                if row["File"] != "No file uploaded":
                    st.markdown(f"[📄 Download File]({row['File']})", unsafe_allow_html=True)
                else:
                    st.info("No file uploaded by this student.")

                st.markdown("---")

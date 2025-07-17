import streamlit as st
import pandas as pd
from utils import load_data

st.title("🧑‍🏫 Supervisor Portal")

if st.session_state.get("role") != "Supervisor":
    st.warning("Access denied. Only supervisors can access this page.")
    st.stop()

df = load_data()

if df.empty:
    st.info("No student data submitted yet.")
else:
    supervisor_name = st.session_state.username
    supervisor_data = df[df["Supervisor"] == supervisor_name]

    st.subheader("Student Submissions")
    st.dataframe(supervisor_data)

    for i, row in supervisor_data.iterrows():
        if row["File"]:
            with open(row["File"], "rb") as f:
                st.download_button(
                    label=f"Download File for {row['Name']}",
                    data=f,
                    file_name=row["File"].split("/")[-1],
                    mime="application/octet-stream"
                )

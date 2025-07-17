import streamlit as st
import pandas as pd
from utils import load_data, init_data_file

init_data_file()

st.title("📊 Supervisor Dashboard")

df = load_data()

if df.empty:
    st.warning("No student data submitted yet.")
else:
    st.subheader("📄 Project Submissions")
    st.dataframe(df)

    st.subheader("🚩 Overdue Projects")
    overdue = df[df["Progress"] < 50]
    if overdue.empty:
        st.success("No overdue projects!")
    else:
        st.error("These projects are below 50% progress:")
        st.dataframe(overdue)

    st.subheader("📂 View Uploaded Files")
    for i, row in df.iterrows():
        st.markdown(f"**{row['Name']} – {row['Project Title']}**")
        st.markdown(f"[Download File]({row['File']})")

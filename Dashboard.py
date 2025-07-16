import streamlit as st
from utils import load_data

st.header("📋 Supervisor Dashboard")
df = load_data()

if df.empty:
    st.warning("No project data found.")
else:
    st.dataframe(df)

    st.markdown("### 📤 Download Excel")
    st.download_button("Export", df.to_excel(index=False, engine='openpyxl'), file_name="fyp_projects.xlsx")

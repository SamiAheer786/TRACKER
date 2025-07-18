import streamlit as st
import pandas as pd
from utils import load_data

def show_supervisor_portal():
    st.title("📊 Supervisor Dashboard")

    df = load_data()

    if df.empty:
        st.warning("No student submissions found.")
        return

    st.subheader("📁 All Submissions")
    st.dataframe(df)

    st.subheader("📈 Analytics Summary")

    if "Supervisor" in df.columns:
        st.markdown("#### 👨‍🏫 Projects per Supervisor")
        st.bar_chart(df['Supervisor'].value_counts())

    if "RegNo" in df.columns:
        st.markdown("#### 📚 Submissions by Registration Number")
        st.line_chart(df['RegNo'].value_counts())

    st.subheader("🔎 Search by Registration Number")
    search_reg = st.text_input("Enter Reg. No to filter:")
    if search_reg:
        filtered = df[df['RegNo'].str.contains(search_reg, case=False, na=False)]
        if not filtered.empty:
            st.dataframe(filtered)
        else:
            st.info("No matching record found.")

import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data, init_data_file

init_data_file()

st.title("📈 Project Analytics")

df = load_data()
if df.empty:
    st.warning("No data available.")
else:
    st.subheader("🎯 Progress Distribution")
    fig = px.histogram(df, x="Progress", nbins=10, title="Project Progress Histogram")
    st.plotly_chart(fig)

    st.subheader("📊 Progress by Supervisor")
    fig2 = px.bar(df, x="Supervisor", y="Progress", color="Name", barmode="group")
    st.plotly_chart(fig2)

    st.subheader("📌 Summary Table")
    st.dataframe(df.groupby("Supervisor")["Progress"].mean().reset_index())

import streamlit as st
from utils import load_data
import plotly.express as px

st.header("📊 Progress Analytics")

df = load_data()

if df.empty:
    st.warning("No data to visualize.")
else:
    col1, col2 = st.columns(2)

    with col1:
        progress_chart = px.histogram(df, x="Progress", nbins=10, title="Progress Distribution")
        st.plotly_chart(progress_chart, use_container_width=True)

    with col2:
        dept_chart = px.pie(df, names="Department", title="Projects per Department")
        st.plotly_chart(dept_chart, use_container_width=True)

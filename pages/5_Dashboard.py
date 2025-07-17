import streamlit as st
import pandas as pd

st.title("📊 Supervisor Dashboard")

# Dummy data for example
data = {
    "Student": ["Ali", "Sara", "Ahmed", "Zara"],
    "Project Title": ["AI Chatbot", "Data Viz", "ML Classifier", "IoT System"],
    "Progress (%)": [85, 60, 40, 95]
}
df = pd.DataFrame(data)

st.subheader("Project Progress Overview")
st.dataframe(df)

st.subheader("Average Progress")
st.metric("Avg Progress", f"{df['Progress (%)'].mean():.2f}%")

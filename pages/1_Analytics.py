import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Analytics & Insights")

# Dummy data for plotting
df = pd.DataFrame({
    "Student": ["Ali", "Sara", "Ahmed", "Zara"],
    "Progress": [85, 60, 40, 95]
})

fig = px.bar(df, x="Student", y="Progress", title="Student Progress Overview", text="Progress")
st.plotly_chart(fig)

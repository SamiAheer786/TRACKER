import streamlit as st
import pandas as pd
import plotly.express as px
from utils import get_all_data

if "role" not in st.session_state or st.session_state.role != "Supervisor":
    st.warning("Access denied.")
    st.stop()

st.title("📊 Project Analytics")

data = get_all_data()

fig = px.bar(data, x="Name", y="Progress", color="Supervisor", title="Student Progress Overview")
st.plotly_chart(fig)

st.markdown("### Overdue Projects")
overdue = data[data["Progress"] < 50]
st.dataframe(overdue)

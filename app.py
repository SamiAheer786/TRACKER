import streamlit as st
from utils import load_data

st.set_page_config(page_title="FYP Tracker", layout="wide")

st.title("🎓 Final Year Project Tracker")
st.subheader("Welcome to the Student–Supervisor FYP Portal")

st.markdown("Navigate through the left menu to access different features:")

st.markdown("""
- 📥 Submit or update your project details
- 📊 View dashboards (for supervisors)
- 📁 Upload your final reports
- 📈 Analyze progress and overdue tasks
- 👨‍👩‍👧 Manage student groups
""")

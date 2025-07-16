import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="FYP Tracker", layout="wide")

st.title("🎓 Final Year Project Tracker")
st.subheader("Welcome to the Student–Supervisor FYP Portal")

st.markdown("Choose your action below:")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📥 Submit / Update Project"):
        switch_page("Group_Management")

with col2:
    if st.button("📁 Upload Final Report"):
        switch_page("Upload_Reports")

with col3:
    if st.button("📊 Supervisor Dashboard"):
        switch_page("Dashboard")

col4, col5 = st.columns([1, 2])
with col4:
    if st.button("📈 Analytics"):
        switch_page("Analytics")

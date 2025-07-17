import streamlit as st
from utils import get_user_history

if "role" not in st.session_state or st.session_state.role != "Student":
    st.warning("Access denied.")
    st.stop()

st.title("📂 Your Submission History")

history = get_user_history(st.session_state.username)

if history.empty:
    st.info("No history found.")
else:
    st.dataframe(history)

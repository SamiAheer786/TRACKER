import streamlit as st
from utils import load_data
import time

def show_supervisor_portal():
    st.title("Supervisor Dashboard")
    st.markdown("Live View of Assigned Student Progress")

    while True:
        data = load_data()
        supervisor_name = "supervisor1"  # Customize based on session if needed
        assigned_data = data[data["Supervisor"] == supervisor_name]

        if not assigned_data.empty:
            for i, row in assigned_data.iterrows():
                with st.expander(f"Student: {row['Name']}"):
                    st.write(f"Project: {row['Project']}")
                    st.write(f"Progress: {row['Progress']}")
                    if row["File"] != "No file uploaded":
                        st.markdown(f"[📄 Download File]({row['File']})", unsafe_allow_html=True)
        else:
            st.info("No data submitted yet.")

        st.markdown("---")
        st.info("Refreshing every 20 seconds...")
        time.sleep(20)
        st.experimental_rerun()

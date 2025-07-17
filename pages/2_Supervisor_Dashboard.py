import streamlit as st
import pandas as pd
from utils import get_all_data

if "role" not in st.session_state or st.session_state.role != "Supervisor":
    st.warning("Access denied.")
    st.stop()

st.title("🧑‍🏫 Supervisor Dashboard")

data = get_all_data()

st.dataframe(data)

# Download links for files
st.markdown("### Downloadable Files")
for index, row in data.iterrows():
    st.markdown(f"**{row['Name']} – {row['Project']}**")
    if row['File'] and row['File'] != "nan":
        with open(row["File"], "rb") as f:
            st.download_button("Download File", f, file_name=row["File"].split("/")[-1])

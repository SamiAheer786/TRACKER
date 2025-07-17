import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="🎓 Final Year Project Tracker", layout="wide")

st.title("🎓 Final Year Project Tracker")
st.markdown("""
Welcome to the **Student–Supervisor FYP Portal**  
Navigate through the left menu to access different features:
- 📥 Submit or update your project details  
- 📊 View dashboards (for supervisors)  
- 📁 Upload your final reports  
- 📈 Analyze progress and overdue tasks  
- 👨‍👩‍👧 Manage student groups  
""")

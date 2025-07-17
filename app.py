import streamlit as st

st.set_page_config(page_title="🎓 FYP Tracker", layout="centered")
st.title("🎓 Final Year Project Tracker")

st.markdown("## 🔐 Login Portal")

role = st.selectbox("Select Role", ["Student", "Supervisor"])
password = st.text_input("Enter Password", type="password")
login_button = st.button("Login")

if login_button:
    if role == "Student" and password == "student123":
        st.success("Login successful as Student")
        st.switch_page("pages/1_Student_Portal.py")
    elif role == "Supervisor" and password == "supervisor123":
        st.success("Login successful as Supervisor")
        st.switch_page("pages/2_Supervisor_Dashboard.py")
    else:
        st.error("Invalid password. Please try again.")

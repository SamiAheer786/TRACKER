import streamlit as st

st.set_page_config(page_title="FYP Tracker", layout="wide")

st.title("🎓 Final Year Project Tracker")
st.subheader("Welcome to the Student–Supervisor FYP Portal")

# Store selected page in session state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Display buttons
if st.session_state.page == "Home":
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("📥 Submit / Update Project"):
            st.session_state.page = "Group_Management"
    with col2:
        if st.button("📁 Upload Final Report"):
            st.session_state.page = "Upload_Reports"
    with col3:
        if st.button("📊 Supervisor Dashboard"):
            st.session_state.page = "Dashboard"

    col4, col5 = st.columns([1, 2])
    with col4:
        if st.button("📈 Analytics"):
            st.session_state.page = "Analytics"

# Dynamically include the target page
if st.session_state.page == "Group_Management":
    import pages.Group_Management as gm
    gm

elif st.session_state.page == "Upload_Reports":
    import pages.Upload_Reports as ur
    ur

elif st.session_state.page == "Dashboard":
    import pages.Dashboard as dash
    dash

elif st.session_state.page == "Analytics":
    import pages.Analytics as ana
    ana

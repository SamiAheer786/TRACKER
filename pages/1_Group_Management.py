import streamlit as st

st.title("👨‍👩‍👧 Group Management")
st.markdown("Manage your group members and assign roles.")

with st.form("group_form"):
    group_name = st.text_input("Group Name")
    member_names = st.text_area("Group Members (one per line)")
    submitted = st.form_submit_button("Save Group")

if submitted:
    st.success(f"Group '{group_name}' saved with {len(member_names.splitlines())} members.")


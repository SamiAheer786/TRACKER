import streamlit as st

# A sample function to save uploaded files (used in Upload_Reports)
def save_uploaded_file(uploaded_file, folder="uploads"):
    import os
    if not os.path.exists(folder):
        os.makedirs(folder)
    file_path = os.path.join(folder, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

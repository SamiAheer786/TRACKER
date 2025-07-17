import os
import pandas as pd

DATA_FILE = "data/project_data.csv"
UPLOAD_DIR = "uploads"

def init_data_file():
    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=["Name", "Project", "Progress", "Supervisor", "File"])
        df.to_csv(DATA_FILE, index=False)
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

def save_uploaded_file(uploaded_file):
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def save_data(new_data):
    df = pd.read_csv(DATA_FILE)
    new_row = pd.DataFrame([new_data])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

def get_all_data():
    return pd.read_csv(DATA_FILE)

def get_user_history(name):
    df = pd.read_csv(DATA_FILE)
    return df[df["Name"] == name]

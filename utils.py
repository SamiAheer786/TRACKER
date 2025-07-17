import pandas as pd
import os

DATA_FILE = "data.csv"
UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

def init_data_file():
    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=["Name", "Project", "Progress", "Supervisor", "File"])
        df.to_csv(DATA_FILE, index=False)

def save_uploaded_file(uploaded_file, student_name):
    filename = f"{student_name}_{uploaded_file.name}"
    file_path = os.path.join(UPLOAD_DIR, filename)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    return file_path

def save_data(new_data):
    df = pd.read_csv(DATA_FILE)
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

def load_data():
    if not os.path.exists(DATA_FILE):
        return pd.DataFrame(columns=["Name", "Project", "Progress", "Supervisor", "File"])
    return pd.read_csv(DATA_FILE)

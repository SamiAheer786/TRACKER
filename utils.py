import os
import pandas as pd

UPLOAD_DIR = "uploads"
CSV_FILE = "submissions.csv"

def save_uploaded_file(uploaded_file):
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
    path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return path

def append_submission(data):
    df = pd.DataFrame([data])
    if os.path.exists(CSV_FILE):
        df_existing = pd.read_csv(CSV_FILE)
        df = pd.concat([df_existing, df], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)

def load_data():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    return pd.DataFrame()

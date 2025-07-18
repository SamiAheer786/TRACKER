import os
import pandas as pd

UPLOAD_FOLDER = "uploads"
DATA_FILE = "submissions.csv"

def save_uploaded_file(uploaded_file):
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    
    with open(path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    return path

def save_data(data):
    df_new = pd.DataFrame([data])
    
    if os.path.exists(DATA_FILE):
        df_existing = pd.read_csv(DATA_FILE)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_combined = df_new
    
    df_combined.to_csv(DATA_FILE, index=False)

def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    return pd.DataFrame()

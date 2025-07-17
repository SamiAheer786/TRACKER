import os
import pandas as pd

DATA_FILE = "data.csv"

def init_data_file():
    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=["Name", "Project Title", "Supervisor", "Progress", "File"])
        df.to_csv(DATA_FILE, index=False)

def load_data():
    return pd.read_csv(DATA_FILE)

def save_data(new_data):
    df = load_data()
    df = df.append(new_data, ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

def save_uploaded_file(uploaded_file):
    folder = "uploads"
    if not os.path.exists(folder):
        os.makedirs(folder)
    filepath = os.path.join(folder, uploaded_file.name)
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return filepath

import os
import pandas as pd

DATA_FILE = "uploads/data.csv"

def init_data_file():
    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=["Name", "Project", "Progress", "Supervisor", "File"])
        df.to_csv(DATA_FILE, index=False)

def save_uploaded_file(uploaded_file):
    path = os.path.join("uploads", uploaded_file.name)
    with open(path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return path

def save_data(new_data):
    df = pd.read_csv(DATA_FILE)
    df.loc[len(df)] = new_data
    df.to_csv(DATA_FILE, index=False)

def load_data():
    return pd.read_csv(DATA_FILE)

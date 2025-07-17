import pandas as pd
import os

DATA_FILE = "data.csv"
UPLOAD_DIR = "uploads"

# Create upload directory if not exists
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

def save_data(new_data, file_path=DATA_FILE):
    # Load existing data if file exists, else create empty DataFrame
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        df = pd.DataFrame()

    # Convert new data dictionary to DataFrame
    new_row = pd.DataFrame([new_data])

    # Concatenate with existing data
    df = pd.concat([df, new_row], ignore_index=True)

    # Save the updated data to CSV
    df.to_csv(file_path, index=False)

def load_data(file_path=DATA_FILE):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        return pd.DataFrame()

def save_uploaded_file(uploaded_file):
    save_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return save_path

import os
import pandas as pd
import uuid

# Constants
UPLOAD_FOLDER = "uploaded_files"
DATA_FILE = "data.csv"

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def init_data_file(file_path=DATA_FILE):
    """Initialize the CSV file if it doesn't exist."""
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=["Name", "Project Name", "Progress", "Supervisor", "File"])
        df.to_csv(file_path, index=False)

def save_uploaded_file(uploaded_file):
    """Save uploaded file to folder and return the saved path."""
    unique_filename = f"{uuid.uuid4().hex}_{uploaded_file.name}"
    file_path = os.path.join(UPLOAD_FOLDER, unique_filename)
    
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path

def save_data(new_data, file_path=DATA_FILE):
    """Save new entry to CSV file."""
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        df = pd.DataFrame(columns=["Name", "Project Name", "Progress", "Supervisor", "File"])

    # Convert new_data dict to single-row DataFrame
    new_row = pd.DataFrame([new_data])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(file_path, index=False)

def load_data(file_path=DATA_FILE):
    """Load all student-submitted project data."""
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        return pd.DataFrame(columns=["Name", "Project Name", "Progress", "Supervisor", "File"])

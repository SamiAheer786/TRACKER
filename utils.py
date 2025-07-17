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

def save_data(new_data, file_path="data.csv"):
    import os
    import pandas as pd

    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        df = pd.DataFrame()

    # Convert new_data (dict) into a DataFrame
    new_row = pd.DataFrame([new_data])

    # Use concat instead of append
    df = pd.concat([df, new_row], ignore_index=True)

    df.to_csv(file_path, index=False)


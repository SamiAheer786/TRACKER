import pandas as pd
import os
from datetime import datetime

DATA_FILE = "fyp_data.csv"

def load_data():
    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=[
            "Group ID", "Student Names", "Department", "Project Title", "Supervisor",
            "Progress", "Deadline", "Last Updated", "Report Link", "Comments"
        ])
        df.to_csv(DATA_FILE, index=False)
    else:
        df = pd.read_csv(DATA_FILE)
    return df

def save_data(df):
    df.to_csv(DATA_FILE, index=False)

def add_or_update_project(group_id, student_names, department, title, supervisor, progress, deadline):
    df = load_data()
    now = datetime.now().strftime("%Y-%m-%d")
    if group_id in df["Group ID"].values:
        df.loc[df["Group ID"] == group_id, [
            "Student Names", "Department", "Project Title", "Supervisor",
            "Progress", "Deadline", "Last Updated"]] = [
            student_names, department, title, supervisor, progress, deadline, now]
    else:
        new_row = pd.DataFrame([{
            "Group ID": group_id, "Student Names": student_names,
            "Department": department, "Project Title": title, "Supervisor": supervisor,
            "Progress": progress, "Deadline": deadline,
            "Last Updated": now, "Report Link": "", "Comments": ""
        }])
        df = pd.concat([df, new_row], ignore_index=True)
    save_data(df)

def overdue_projects():
    df = load_data()
    today = datetime.now().date()
    if "Deadline" not in df.columns:
        return pd.DataFrame()
    try:
        df["Deadline"] = pd.to_datetime(df["Deadline"], errors="coerce")
        df = df.dropna(subset=["Deadline"])
        df["Overdue"] = df["Deadline"].apply(lambda x: x.date() < today if pd.notnull(x) else False)
        return df[df["Overdue"]]
    except:
        return pd.DataFrame()

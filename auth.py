def login(username, password):
    users = {
        "student1": {"password": "studentpass", "role": "Student"},
        "supervisor1": {"password": "supervisorpass", "role": "Supervisor"},
    }

    user = users.get(username)
    if user and user["password"] == password:
        return user["role"]
    return None

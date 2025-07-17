# Hardcoded credentials
users = {
    "student1": {"password": "student123", "role": "Student"},
    "supervisor1": {"password": "super123", "role": "Supervisor"},
}

def login(username, password):
    user = users.get(username)
    if user and user["password"] == password:
        return user["role"]
    return None

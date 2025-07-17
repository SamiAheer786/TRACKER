users = {
    "student1": {"password": "student123", "role": "Student"},
    "supervisor1": {"password": "super123", "role": "Supervisor"},
}

def login(username, password):
    user = users.get(username)
    if user and user["password"] == password:
        return user["role"]
    return None

def get_user_role(username):
    user = users.get(username)
    if user:
        return user["role"]
    return None

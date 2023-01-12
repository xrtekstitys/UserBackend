import json
from user import User

def get_database_content():
    with open("database.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    return data

def get_user(username):
    data = get_database_content()
    user_data = {}
    if username in data:
        user_data = data[username]

    return user_data

def is_password_right(username, password):
    data = get_user(username)
    if data == password:
        return True
    return False

def create_user(user: User):
    # TODO #1 Remember to check if user already exists
    data = get_database_content()
    data[user.username] = user.password
    with open("database.json", "w") as f:
        json.dump(data, f)
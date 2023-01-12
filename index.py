from flask import Flask, jsonify, request, abort
from db import create_user, is_password_right
import json
from user import User

app = Flask(__name__)


@app.route("/user/", methods=["POST", "GET"])
def user():
    if request.method == "GET":
        user_data = request.json()
        return json.dumps({"is_password_right": is_password_right(username=user_data["username"], password=user_data["password"])})
    if request.method == "POST":
        user_data = request.json()
        username = user_data["username"]
        password = user_data["password"]
        create_user(User(username, password))
        return json.dumps({"status": "okay"})

    if not request.method in ["POST", "GET"]:
        abort(500)


if __name__ == '__main__':

    app.run(debug=True)

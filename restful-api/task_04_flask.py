#!/usr/bin/python3
"""
Module implementing a simple REST API using the Flask framework.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """
    Handles the root endpoint and returns a welcome message.
    """
    return "Welcome to the Flask API!"


@app.route("/status")
def get_status():
    """
    Returns the operational status of the API.
    """
    return "OK"


@app.route("/data")
def get_data():
    """
    Returns a JSON list of all stored usernames.
    """
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """
    Retrieves the full user object corresponding to the provided username.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Parses incoming JSON data to add a new user to the API.
    """
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    response_data = {"message": "User added", "user": data}
    return jsonify(response_data), 201


if __name__ == "__main__":
    app.run()

from flask import Blueprint, request, jsonify, session
import bcrypt

auth = Blueprint('auth', _name_)

# Simulate a user database
users_db = {}

# Sign up endpoint
@auth.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data['username']
    password = data['password']

    if username in users_db:
        return jsonify({"error": "User already exists"}), 400

    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    users_db[username] = hashed_pw
    return jsonify({"message": "User created successfully"}), 200

# Login endpoint
@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    if username not in users_db or not bcrypt.checkpw(password.encode('utf-8'), users_db[username]):
        return jsonify({"error": "Invalid credentials"}), 401

    session['user'] = username
    return jsonify({"message": "Login successful"}), 200

# Logout endpoint
@auth.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    return jsonify({"message": "Logged out successfully"}), 200
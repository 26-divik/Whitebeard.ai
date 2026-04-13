from flask import app, jsonify, request,session
from app.controller.db_controller.sql_controller import add_user, get_user_by_email
import re  
import bcrypt
import flask_session as Session
def signup():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400

    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({"error": "Invalid JSON format"}), 400

    if not isinstance(data, dict):
        return jsonify({"error": "JSON must be an object"}), 400
        
    is_valid, message = validate_signup_data(data)
    if not is_valid:
        return jsonify({"error": message}), 400

    hashed, hashed_password = gethash(data)
    if not hashed:
        return jsonify({"error": hashed_password}), 400
    else:
        success, msg = add_user(data['email'], hashed_password, data['name'])
        if not success:
            return jsonify({"error": msg}), 400
    return jsonify({"message": "Signup successful"}), 201

def validate_signup_data(data):
    print(type(data))
    special_characters = "!@#$%^&*()-+?_=,<>/\"'"
    required_fields = ['email', 'password', 'name']
    for field in required_fields:
        if field not in data  or not data[field]:
            return False, f"{field} is required"
    email = data.get('email').strip().lower()
    password = data.get('password')
    name = data.get('name').strip().lower()
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False, "Invalid email format"
    if len(password) < 6 or not any(char.isupper() for char in password) or not any(char in special_characters for char in password):
        return False, "Password must have at least 6 characters,one capital letter and one special character."
    if get_user_by_email(email) is not None:
        return False, "Email already exists"
    return True, "Validation successful"
def gethash(data):
    password = data.get('password')
    try:
        bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(bytes, salt).decode('utf-8')
        return True, hashed_password
    except Exception as e:
        return False, str(e)
    
def login():
    data = request.get_json(silent=True) or {}
    is_valid, message = validate_login_data(data)
    if not is_valid:
        return jsonify({"error": message}), 400
    email = data.get('email').strip().lower()
    user = get_user_by_email(email)
    if not user:
        return jsonify({"error": "Email does not exist"}), 400
    password = data.get('password') 
    hashed_password = user['password']
    if not check_hashed_password(password, hashed_password):
        return jsonify({"error": "Invalid password"}), 400
    session['user_id'] = user['id']
    return jsonify({"message": "Login successful"}),200

def validate_login_data(data):
    required_fields = ['email', 'password']
    for field in required_fields:
        if field not in data  or not data[field]:
            return False, f"{field} is required"
    return True, "Validation successful"

def check_hashed_password(password, hashed_password):
    try:
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
    except Exception as e:
        return False
    
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Logout successful"}), 200
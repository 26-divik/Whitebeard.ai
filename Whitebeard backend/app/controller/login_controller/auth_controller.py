from flask import jsonify, request
from app.controller.db_controller.db_controller import add_user, check_user_exists
import re  
import bcrypt
def signup():
    data = request.get_json(silent=True) or {}
    is_valid, message = validate_signup_data(data)
    if not is_valid:
        return jsonify({"error": message}), 400

    hashed, hashed_password = gethash(data)
    if not hashed:
        return jsonify({"error": hashed_password}), 400
    else:
        success, msg = add_user(data['username'], data['email'], hashed_password, data['name'])
        if not success:
            return jsonify({"error": msg}), 400
    return jsonify({"message": "Signup successful"}), 201

def validate_signup_data(data):
    special_characters = "!@#$%^&*()-+?_=,<>/\"'"
    required_fields = ['username', 'email', 'password', 'name']
    for field in required_fields:
        if field not in data  or not data[field]:
            return False, f"{field} is required"
    username = data.get('username').strip().lower()
    email = data.get('email').strip().lower()
    password = data.get('password')
    name = data.get('name').strip().lower()
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False, "Invalid email format"
    if len(password) < 6 or not any(char.isupper() for char in password) or not any(char in special_characters for char in password):
        return False, "Password must have at least 6 characters,one capital letter and one special character."
    user_u, user_e = check_user_exists(username, email)  
    if user_u:
        return False, "Username already exists"
    if user_e:
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
    

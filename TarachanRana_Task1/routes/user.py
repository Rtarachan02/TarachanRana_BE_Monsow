# routes/user.py
from flask import Blueprint, request, jsonify
import bcrypt

user_routes = Blueprint('user', __name__)

users = []

@user_routes.route('/register', methods=['POST'])
def register_user():
    data = request.json
    
    # Validate input
    if 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Missing fields'}), 400
    
    username = data['username']
    email = data['email']
    password = data['password']
    
    # Basic validation
    if len(password) < 8:
        return jsonify({'error': 'Password must be at least 8 characters long'}), 400
    
    # Hash and encrypt the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    # Save user information (including hashed password)
    users.append({'username': username, 'email': email, 'password': hashed_password.decode('utf-8')})
    
    return jsonify({'message': 'User registered successfully'}), 200

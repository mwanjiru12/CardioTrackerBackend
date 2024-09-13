from flask import Blueprint, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, decode_token
from ..models import User
from .. import db

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Ensure all required fields are present
    if not data or not all(key in data for key in ('username', 'password', 'name', 'location')):
        return jsonify({'message': 'All fields (username, password, name, location) are required.'}), 400  # Bad Request

    username = data.get('username')
    password_raw = data.get('password')
    name = data.get('name')
    location = data.get('location')

    # Check if the username already exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'Username already exists. Please choose another one.'}), 409  # Conflict

    # Generate hashed password
    password = generate_password_hash(password_raw)

    # Create a new user if username doesn't exist
    new_user = User(username=username, password=password, name=name, location=location)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully', 'username': username}), 201

@bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        user = User.query.filter_by(username=data['username']).first()

        if user and check_password_hash(user.password, data['password']):
            access_token = create_access_token(identity=user.id)  # Create JWT token
            return jsonify({
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'name': user.name,
                    'location': user.location
                },
                'access_token': access_token  # Include JWT token in the response
            }), 200

        return jsonify({'message': 'Invalid credentials'}), 401

    except Exception as e:
        print(f"Error during login: {str(e)}")
        return jsonify({'message': 'Internal Server Error'}), 500

@bp.route('/protected', methods=['GET'])
@jwt_required()
def protected_route():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify({
        'id': user.id,
        'username': user.username,
        'name': user.name,
        'location': user.location
    }), 200

@bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    user_id = get_jwt_identity()  # Get the user ID from the JWT token
    user = User.query.get(user_id)  # Query the database for the user

    if user:
        return jsonify({
            'user': {
                'id': user.id,
                'username': user.username,
                'location': user.location,
                'name': user.name
            }
        }), 200
    else:
        return jsonify({'message': 'User not found.'}), 404

@bp.route('/auto_login', methods=['POST'])
def auto_login():
    data = request.json
    jwt_token = data.get('jwt')

    if not jwt_token:
        return jsonify({'message': 'JWT is required'}), 400

    try:
        # Decode the JWT token
        decoded_token = decode_token(jwt_token)
        user_id = decoded_token['sub']  # Adjust based on how the JWT is structured
        
        # Query the database for the user
        user = User.query.get(user_id)
        if user:
            return jsonify({
                'id': user.id,
                'username': user.username,
                'location': user.location,
                'name': user.name
            }), 200
        else:
            return jsonify({'message': 'User not found.'}), 404

    except Exception as e:
        # Log the exception for debugging
        print(f"Error: {e}")
        return jsonify({'message': 'Invalid or expired token.'}), 401
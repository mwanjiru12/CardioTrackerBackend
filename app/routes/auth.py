from flask import Blueprint, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, decode_token
from ..models import User
from .. import db

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = generate_password_hash(data.get('password'))
    name = data.get('name')
    location = data.get('location')

    # Check if the username already exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'Username already exists. Please choose another one.'}), 409  # Conflict

    # Create a new user if username doesn't exist
    new_user = User(username=username, password=password, name=name, location=location)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()

    if user and check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.id)  # Create JWT token
        response = make_response(jsonify({
            'user': {
                'id': user.id,
                'username': user.username,
                'name': user.name,
                'location': user.location
            },
            'access_token': access_token  # Include JWT token in the response
        }))
        response.set_cookie('access_token', access_token, httponly=True)  # Optional: Set token in cookie
        return response

    return jsonify({'message': 'Invalid credentials'}), 401

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
        # Decode the JWT to get the user_id
        decoded_token = decode_token(jwt_token)  # Correct method to use
        user_id = decoded_token['identity']  # Adjust based on how the JWT is structured
        
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
        return jsonify({'message': 'Invalid or expired token.'}), 401

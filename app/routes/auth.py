from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from ..models import User  # Correct import for User model
from .. import db  # Correct import for db from the app package

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    password = generate_password_hash(data['password'])
    name = data['name']
    location = data.get('location')

    new_user = User(username=username, password=password, name=name, location=location)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()

    if user and check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify({
            'user': {'id': user.id, 'username': user.username, 'name': user.name, 'location': user.location},
            'jwt': access_token
        }), 200
    return jsonify({'message': 'Invalid credentials'}), 401

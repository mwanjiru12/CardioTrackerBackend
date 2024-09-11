from flask import Blueprint, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
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
        response = make_response(jsonify({
            'user': {'id': user.id, 'username': user.username, 'name': user.name, 'location': user.location}
        }))
        response.set_cookie('access_token', access_token, httponly=True)
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


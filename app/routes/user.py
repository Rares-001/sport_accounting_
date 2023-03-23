from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from models.user import User

user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify({'users': [u.to_dict() for u in users]})

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    password = data.pop('password')
    hashed_password = generate_password_hash(password)
    user = User(password=hashed_password, **data)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict())

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    password = data.pop('password', None)
    if password:
        user.password = generate_password_hash(password)
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return jsonify(user.to_dict())

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': f'User {user_id} has been deleted.'})


from flask import Blueprint, request, jsonify
from app.extensions import bcrypt, db
from app.models import User
from .schemas import UserSchema, LoginSchema
from flask_jwt_extended import create_access_token, create_refresh_token


auth_bp = Blueprint('auth', __name__)
user_schema = UserSchema()
login_schema = LoginSchema()

@auth_bp.route('/register', methods=['POST'])
def register_users():
    data = user_schema.load(request.json)

    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    user = User(
        name = data['name'],
        email = data['email'],
        password = hashed_password
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login_users():
    data = login_schema.load(request.json)

    user = User.query.filter_by(email=data['email']).first()
    if not user or not bcrypt.check_password_hash(user.password, data['password']):
        return jsonify({"error": "Invalid credentials"}), 401
    
    access_token = create_access_token(identity=str(user.id))
    refresh_token = create_refresh_token(identity=str(user.id))

    return jsonify({
        "access_token": access_token,
        "refresh_token": refresh_token
    }), 200
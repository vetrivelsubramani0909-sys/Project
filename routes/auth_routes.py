from flask import Blueprint, request, jsonify
from extensions import db
from models import Admin
from utils import hash_password, verify_password
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed = hash_password(data['password'])
    admin = Admin(username=data['username'], password=hashed)
    db.session.add(admin)
    db.session.commit()
    return jsonify({"message": "Admin registered"})

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    admin = Admin.query.filter_by(username=data['username']).first()

    if admin and verify_password(data['password'], admin.password):
        token = create_access_token(identity=admin.id)
        return jsonify(access_token=token)

    return jsonify({"error": "Invalid credentials"}), 401
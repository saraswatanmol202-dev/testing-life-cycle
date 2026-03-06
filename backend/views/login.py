# Epic Title: Implement Secure Login Mechanism

from flask import Blueprint, request, jsonify
from models.user import User
from werkzeug.security import check_password_hash

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data.get('username')).first()
    if user and check_password_hash(user.password, data.get('password')):
        return jsonify({"message": "Password correct", "user_id": user.id}), 200
    return jsonify({"message": "Invalid credentials"}), 401
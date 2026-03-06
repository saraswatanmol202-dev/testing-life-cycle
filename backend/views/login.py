# Epic Title: Create Secure User Sessions

from flask import Blueprint, request, jsonify, session
from models.user import User
from models.session import Session
from werkzeug.security import check_password_hash
from backend import db

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/login', methods=['POST'])
def login():
    data = request.form
    user = User.query.filter_by(username=data.get('username')).first()
    if user and check_password_hash(user.password, data.get('password')):
        user_session = Session(user_id=user.id)
        db.session.add(user_session)
        db.session.commit()
        session['user_id'] = user.id
        return jsonify({"message": "Login successful", "user_id": user.id}), 200
    return jsonify({"message": "Invalid credentials"}), 401
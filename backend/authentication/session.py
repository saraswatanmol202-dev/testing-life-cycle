# Epic Title: Create Secure User Sessions

from datetime import timedelta
from flask import Blueprint, session, redirect, url_for
from flask import current_app
from models.session import Session
from backend import db

session_blueprint = Blueprint('session', __name__)

@session_blueprint.before_app_request
def make_session_permanent():
    session.permanent = True
    current_app.permanent_session_lifetime = timedelta(minutes=15)
    session.modified = True

@session_blueprint.route('/extend_session', methods=['GET'])
def extend_session():
    session.modified = True
    return {"message": "Session extended"}, 200

@session_blueprint.route('/logout', methods=['POST'])
def logout():
    user_id = session.pop('user_id', None)
    if user_id:
        active_session = Session.query.filter_by(user_id=user_id).first()
        if active_session:
            db.session.delete(active_session)
            db.session.commit()
        return {"message": "Logged out"}, 200
    return {"message": "No active session"}, 400
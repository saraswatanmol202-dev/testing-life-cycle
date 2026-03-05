# Epic Title: Real-time Status Updates

from flask import Blueprint, render_template, session, jsonify
from typing import List

# Importing models
from backend.models.notification import Notification

notifications_bp = Blueprint('notifications', __name__)

# Dummy data function for demo purpose
def get_user_notifications(user_id: int) -> List[Notification]:
    # Simulate retrieving notifications from the database
    return [
        Notification(notification_id=1, user_id=user_id, message="Your request has been approved."),
        Notification(notification_id=2, user_id=user_id, message="Your service modification is under process.")
    ]

@notifications_bp.route('/notifications', methods=['GET'])
def notifications():
    user_id = session.get('user_id')
    if not user_id:
        return "Access Denied", 403

    notifications = get_user_notifications(user_id)
    return render_template('notifications.html', notifications=notifications)

@notifications_bp.route('/api/notifications', methods=['GET'])
def api_notifications():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "Access Denied"}), 403

    notifications = get_user_notifications(user_id)
    notifications_data = [{"id": n.notification_id, "message": n.message, "read": n.read, "created_at": n.created_at} for n in notifications]
    return jsonify(notifications_data)
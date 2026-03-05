# Epic Title: In-app Notifications

from flask import Blueprint, render_template, session, jsonify
from typing import List

# Importing models
from backend.models.in_app_notification import InAppNotification

in_app_notifications_bp = Blueprint('in_app_notifications', __name__)

# Dummy data function for demo purpose
def get_user_notifications(user_id: int) -> List[InAppNotification]:
    # Simulate retrieving notifications from the database
    return [
        InAppNotification(notification_id=1, user_id=user_id, message="Your request has been updated."),
        InAppNotification(notification_id=2, user_id=user_id, message="Your request has been completed.")
    ]

@in_app_notifications_bp.route('/in_app_notifications', methods=['GET'])
def in_app_notifications():
    user_id = session.get('user_id')
    if not user_id:
        return "Access Denied", 403

    notifications = get_user_notifications(user_id)
    return render_template('in_app_notifications.html', notifications=notifications)

@in_app_notifications_bp.route('/api/in_app_notifications', methods=['GET'])
def api_in_app_notifications():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "Access Denied"}), 403

    notifications = get_user_notifications(user_id)
    notifications_data = [{"id": n.notification_id, "message": n.message, "read": n.read, "created_at": n.created_at} for n in notifications]
    return jsonify(notifications_data)
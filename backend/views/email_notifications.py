# Epic Title: Email Notifications

from flask import Blueprint, jsonify, request, session
import smtplib
from email.mime.text import MIMEText
from typing import List

# Importing models
from backend.models.email_notification import EmailNotification

email_notifications_bp = Blueprint('email_notifications', __name__)

# Dummy data function for demo purpose
def create_email_notification(user_id: int, subject: str, body: str) -> EmailNotification:
    # Simulate creating a notification
    return EmailNotification(email_id=1, user_id=user_id, subject=subject, body=body, status="Pending")

def send_email(subject: str, recipient: str, body: str) -> None:
    sender = 'noreply@portal.com'
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    with smtplib.SMTP('localhost') as server:
        server.sendmail(sender, [recipient], msg.as_string())

@email_notifications_bp.route('/send_notification', methods=['POST'])
def send_notification():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "Access Denied"}), 403

    data = request.json
    subject = data.get('subject')
    body = data.get('body')
    recipient = data.get('recipient_email')

    # Create email notification
    notification = create_email_notification(user_id, subject, body)

    # Send email
    send_email(subject, recipient, body)

    # Mark notification as sent
    notification.update_status("Sent")

    return jsonify({"message": "Email sent successfully."})
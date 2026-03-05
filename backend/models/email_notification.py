# Epic Title: Email Notifications

from datetime import datetime

class EmailNotification:
    def __init__(self, email_id: int, user_id: int, subject: str, body: str, status: str):
        self.email_id = email_id
        self.user_id = user_id
        self.subject = subject
        self.body = body
        self.status = status
        self.created_at = datetime.utcnow()

    def update_status(self, new_status: str) -> None:
        self.status = new_status
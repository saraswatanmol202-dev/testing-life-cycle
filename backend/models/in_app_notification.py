# Epic Title: In-app Notifications

from datetime import datetime

class InAppNotification:
    def __init__(self, notification_id: int, user_id: int, message: str, read: bool = False):
        self.notification_id = notification_id
        self.user_id = user_id
        self.message = message
        self.read = read
        self.created_at = datetime.utcnow()

    def mark_as_read(self):
        self.read = True
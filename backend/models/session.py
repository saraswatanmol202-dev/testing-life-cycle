# Epic Title: Create Secure User Sessions

from datetime import datetime, timedelta
from typing import Optional

class Session:
    def __init__(self, session_id: str, user_id: int, is_active: bool, last_activity: Optional[datetime] = None):
        self.session_id = session_id
        self.user_id = user_id
        self.is_active = is_active
        self.created_at = datetime.utcnow()
        self.updated_at: Optional[datetime] = None
        self.last_activity = last_activity if last_activity else datetime.utcnow()

    def is_expired(self) -> bool:
        return datetime.utcnow() - self.last_activity >= timedelta(minutes=15)

    def update_activity(self) -> None:
        self.last_activity = datetime.utcnow()
        self.updated_at = self.last_activity
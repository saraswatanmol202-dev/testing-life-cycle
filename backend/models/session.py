# Epic Title: Implement Secure Login Mechanism

from datetime import datetime
from typing import Optional

class Session:
    def __init__(self, session_id: str, user_id: int, is_active: bool):
        self.session_id = session_id
        self.user_id = user_id
        self.is_active = is_active
        self.created_at = datetime.utcnow()
        self.updated_at: Optional[datetime] = None
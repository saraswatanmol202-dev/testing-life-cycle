# Epic Title: Implement Secure Login Mechanism

from datetime import datetime
from typing import Optional

class User:
    def __init__(self, user_id: int, username: str, password_hash: str, mfa_enabled: bool):
        self.user_id = user_id
        self.username = username
        self.password_hash = password_hash
        self.mfa_enabled = mfa_enabled
        self.created_at = datetime.utcnow()
        self.updated_at: Optional[datetime] = None
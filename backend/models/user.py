# Epic Title: Manage Secure Storage of Credentials

from datetime import datetime
from typing import Optional
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self, user_id: int, username: str, password: str, mfa_enabled: bool):
        self.user_id = user_id
        self.username = username
        self.password_hash = self._encrypt_password(password)
        self.mfa_enabled = mfa_enabled
        self.created_at = datetime.utcnow()
        self.updated_at: Optional[datetime] = None

    def _encrypt_password(self, password: str) -> str:
        return generate_password_hash(password)

    def verify_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)
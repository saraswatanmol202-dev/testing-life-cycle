# Epic Title: Create Secure User Sessions

from typing import Optional
from datetime import datetime

# Importing Session model
from backend.models.session import Session

class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self, user_id: int) -> Session:
        session = Session(session_id=str(user_id), user_id=user_id, is_active=True)
        self.sessions[user_id] = session
        return session

    def get_session(self, user_id: int) -> Optional[Session]:
        return self.sessions.get(user_id)

    def refresh_session(self, user_id: int) -> bool:
        session = self.get_session(user_id)
        if session:
            if session.is_expired():
                self.end_session(user_id)
                return False
            session.update_activity()
            return True
        return False

    def end_session(self, user_id: int) -> None:
        session = self.get_session(user_id)
        if session:
            session.is_active = False
            session.updated_at = datetime.utcnow()
            # Remove from active sessions
            del self.sessions[user_id]
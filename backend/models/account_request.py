# Epic Title: Streamline Account Opening Requests

from datetime import datetime

class AccountRequest:
    def __init__(self, request_id: int, user_id: int, account_type: str, status: str):
        self.request_id = request_id
        self.user_id = user_id
        self.account_type = account_type
        self.status = status
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
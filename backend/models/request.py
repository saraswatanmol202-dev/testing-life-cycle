# Epic Title: Approval and Processing Workflows

from datetime import datetime
from typing import Optional

class Request:
    def __init__(self, request_id: int, user_id: int, request_type: str, status: str):
        self.request_id = request_id
        self.user_id = user_id
        self.request_type = request_type
        self.status = status
        self.created_at = datetime.utcnow()
        self.updated_at: Optional[datetime] = None

    def set_status(self, status: str):
        self.status = status
        self.updated_at = datetime.utcnow()
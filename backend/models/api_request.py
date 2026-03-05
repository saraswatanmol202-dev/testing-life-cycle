# Epic Title: Develop Secure APIs

from datetime import datetime

class APIRequest:
    def __init__(self, request_id: int, user_id: int, endpoint: str, request_body: str, response_body: str, status: str, created_at: datetime):
        self.request_id = request_id
        self.user_id = user_id
        self.endpoint = endpoint
        self.request_body = request_body
        self.response_body = response_body
        self.status = status
        self.created_at = created_at
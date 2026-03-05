# Epic Title: Maintain Separate Database

from datetime import datetime

class LocalData:
    def __init__(self, data_id: int, user_id: int, data_type: str, content: str, created_at: datetime):
        self.data_id = data_id
        self.user_id = user_id
        self.data_type = data_type
        self.content = content
        self.created_at = created_at
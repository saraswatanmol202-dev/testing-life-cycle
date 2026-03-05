# Epic Title: Maintain Interaction History

from datetime import datetime

class InteractionHistory:
    def __init__(self, history_id: int, user_id: int, action: str, timestamp: datetime):
        self.history_id = history_id
        self.user_id = user_id
        self.action = action
        self.timestamp = timestamp
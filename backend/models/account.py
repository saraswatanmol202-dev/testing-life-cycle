# Epic Title: Develop a User-Friendly Dashboard

from datetime import datetime
from typing import Optional

class Account:
    def __init__(self, account_id: int, user_id: int, account_type: str, balance: float):
        self.account_id = account_id
        self.user_id = user_id
        self.account_type = account_type
        self.balance = balance
        self.created_at = datetime.utcnow()
        self.updated_at: Optional[datetime] = None
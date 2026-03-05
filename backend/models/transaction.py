# Epic Title: Develop a User-Friendly Dashboard

from datetime import datetime

class Transaction:
    def __init__(self, transaction_id: int, account_id: int, amount: float, transaction_type: str, date: datetime):
        self.transaction_id = transaction_id
        self.account_id = account_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.date = date
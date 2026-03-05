# Epic Title: Data Synchronization Mechanisms

from datetime import datetime

class SynchronizationLog:
    def __init__(self, sync_id: int, sync_type: str, status: str, details: str, created_at: datetime):
        self.sync_id = sync_id
        self.sync_type = sync_type
        self.status = status
        self.details = details
        self.created_at = created_at
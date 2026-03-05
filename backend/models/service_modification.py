# Epic Title: Service Modification Requests

from datetime import datetime

class ServiceModification:
    def __init__(self, modification_id: int, user_id: int, service_type: str, status: str):
        self.modification_id = modification_id
        self.user_id = user_id
        self.service_type = service_type
        self.status = status
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
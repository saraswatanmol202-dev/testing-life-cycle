# Epic Title: Document Upload Capability

from datetime import datetime

class Document:
    def __init__(self, document_id: int, user_id: int, filename: str, upload_path: str, upload_date: datetime):
        self.document_id = document_id
        self.user_id = user_id
        self.filename = filename
        self.upload_path = upload_path
        self.upload_date = upload_date
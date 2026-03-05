# Epic Title: Save and Resume Incomplete Applications

from datetime import datetime

class Application:
    def __init__(self, application_id: int, user_id: int, content: str, status: str, last_modified: datetime):
        self.application_id = application_id
        self.user_id = user_id
        self.content = content
        self.status = status
        self.last_modified = last_modified

    def update_content(self, new_content: str):
        self.content = new_content
        self.last_modified = datetime.utcnow()

    def update_status(self, new_status: str):
        self.status = new_status
        self.last_modified = datetime.utcnow()
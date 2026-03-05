# Epic Title: Customizable Widgets

from datetime import datetime

class Widget:
    def __init__(self, widget_id: int, user_id: int, widget_type: str):
        self.widget_id = widget_id
        self.user_id = user_id
        self.widget_type = widget_type
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
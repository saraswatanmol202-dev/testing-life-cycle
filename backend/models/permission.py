# Epic Title: Assign Permissions to Roles

class Permission:
    def __init__(self, permission_id: int, name: str, description: str):
        self.permission_id = permission_id
        self.name = name
        self.description = description
# Epic Title: Assign Permissions to Roles

class RolePermission:
    def __init__(self, role_permission_id: int, role_id: int, permission_id: int):
        self.role_permission_id = role_permission_id
        self.role_id = role_id
        self.permission_id = permission_id
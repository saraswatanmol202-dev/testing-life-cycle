# Epic Title: Access Policies for Different Roles

class RolePolicy:
    def __init__(self, role_policy_id: int, role_id: int, policy_id: int):
        self.role_policy_id = role_policy_id
        self.role_id = role_id
        self.policy_id = policy_id
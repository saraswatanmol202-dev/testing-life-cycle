# Epic Title: Access Policies for Different Roles

CREATE TABLE role_policies (
    role_policy_id INT AUTO_INCREMENT PRIMARY KEY,
    role_id INT,
    policy_id INT,
    FOREIGN KEY (role_id) REFERENCES roles(role_id),
    FOREIGN KEY (policy_id) REFERENCES policies(policy_id)
);
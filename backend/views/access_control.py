# Epic Title: Access Policies for Different Roles

from flask import Blueprint, request, session, jsonify, render_template, redirect, url_for
from typing import List
import logging

# Importing models
from backend.models.policy import Policy
from backend.models.role_policy import RolePolicy
from backend.models.role import Role

access_control_bp = Blueprint('access_control', __name__)

# Dummy functions for demo purpose
def save_policy(name: str, description: str) -> Policy:
    # Simulate saving the policy to the database
    return Policy(policy_id=1, name=name, description=description)

def get_all_policies() -> List<Policy]:
    # Simulate retrieving policies from the database
    return [
        Policy(policy_id=1, name="view_dashboard", description="Can view dashboard"),
        Policy(policy_id=2, name="edit_profile", description="Can edit own profile")
    ]

def assign_policy_to_role(role_id: int, policy_id: int) -> RolePolicy:
    # Simulate assigning a policy to a role
    return RolePolicy(role_policy_id=1, role_id=role_id, policy_id=policy_id)

@access_control_bp.route('/policies', methods=['GET', 'POST'])
def manage_policies():
    admin_id = session.get('admin_id')
    if not admin_id:
        return "Access Denied", 403

    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')

        # Save policy
        policy = save_policy(name, description)
        return redirect(url_for('access_control.manage_policies'))

    policies = get_all_policies()
    return render_template('policy_management.html', policies=policies)

@access_control_bp.route('/assign_policy', methods=['POST'])
def assign_policy():
    admin_id = session.get('admin_id')
    if not admin_id:
        return jsonify({"error": "Access Denied"}), 403

    role_id = request.form.get('role_id')
    policy_id = request.form.get('policy_id')

    try:
        role_policy = assign_policy_to_role(int(role_id), int(policy_id))
        return jsonify({"message": "Policy assigned successfully", "role_policy_id": role_policy.role_policy_id})
    except Exception as e:
        logging.error(f"Error assigning policy to role: {e}")
        return jsonify({"error": str(e)}), 500
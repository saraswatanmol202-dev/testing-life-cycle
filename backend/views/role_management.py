# Epic Title: Define User Roles

from flask import Blueprint, request, session, jsonify, render_template, redirect, url_for
from typing import List
import logging

# Importing models
from backend.models.role import Role
from backend.models.user_role import UserRole

role_management_bp = Blueprint('role_management', __name__)

# Dummy functions for demo purpose
def save_role(name: str, description: str) -> Role:
    # Simulate saving the role to the database
    return Role(role_id=1, name=name, description=description)

def get_all_roles() -> List[Role]:
    # Simulate retrieving roles from the database
    return [
        Role(role_id=1, name="Admin", description="Administrator with full access"),
        Role(role_id=2, name="User", description="Regular user with limited access")
    ]

def assign_role_to_user(user_id: int, role_id: int) -> UserRole:
    # Simulate assigning a role to a user
    return UserRole(user_role_id=1, user_id=user_id, role_id=role_id)

@role_management_bp.route('/roles', methods=['GET', 'POST'])
def manage_roles():
    admin_id = session.get('admin_id')
    if not admin_id:
        return "Access Denied", 403

    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')

        # Save role
        role = save_role(name, description)
        return redirect(url_for('role_management.manage_roles'))

    roles = get_all_roles()
    return render_template('role_management.html', roles=roles)

@role_management_bp.route('/assign_role', methods=['POST'])
def assign_role():
    admin_id = session.get('admin_id')
    if not admin_id:
        return jsonify({"error": "Access Denied"}), 403

    user_id = request.form.get('user_id')
    role_id = request.form.get('role_id')

    try:
        user_role = assign_role_to_user(int(user_id), int(role_id))
        return jsonify({"message": "Role assigned successfully", "user_role_id": user_role.user_role_id})
    except Exception as e:
        logging.error(f"Error assigning role to user: {e}")
        return jsonify({"error": str(e)}), 500
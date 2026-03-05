# Epic Title: Assign Permissions to Roles

from flask import Blueprint, request, session, jsonify, render_template, redirect, url_for
from typing import List
import logging

# Importing models
from backend.models.permission import Permission
from backend.models.role_permission import RolePermission
from backend.models.role import Role

permission_assignment_bp = Blueprint('permission_assignment', __name__)

# Dummy functions for demo purpose
def save_permission(name: str, description: str) -> Permission:
    # Simulate saving the permission to the database
    return Permission(permission_id=1, name=name, description=description)

def get_all_permissions() -> List[Permission]:
    # Simulate retrieving permissions from the database
    return [
        Permission(permission_id=1, name="view_dashboard", description="Can view dashboard"),
        Permission(permission_id=2, name="edit_profile", description="Can edit own profile")
    ]

def assign_permission_to_role(role_id: int, permission_id: int) -> RolePermission:
    # Simulate assigning a permission to a role
    return RolePermission(role_permission_id=1, role_id=role_id, permission_id=permission_id)

@permission_assignment_bp.route('/permissions', methods=['GET', 'POST'])
def manage_permissions():
    admin_id = session.get('admin_id')
    if not admin_id:
        return "Access Denied", 403

    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')

        # Save permission
        permission = save_permission(name, description)
        return redirect(url_for('permission_assignment.manage_permissions'))

    permissions = get_all_permissions()
    return render_template('permission_management.html', permissions=permissions)

@permission_assignment_bp.route('/assign_permission', methods=['POST'])
def assign_permission():
    admin_id = session.get('admin_id')
    if not admin_id:
        return jsonify({"error": "Access Denied"}), 403

    role_id = request.form.get('role_id')
    permission_id = request.form.get('permission_id')

    try:
        role_permission = assign_permission_to_role(int(role_id), int(permission_id))
        return jsonify({"message": "Permission assigned successfully", "role_permission_id": role_permission.role_permission_id})
    except Exception as e:
        logging.error(f"Error assigning permission to role: {e}")
        return jsonify({"error": str(e)}), 500
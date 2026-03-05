# Epic Title: Service Modification Requests

from flask import Blueprint, render_template, request, redirect, url_for, session
from typing import List

# Importing models
from backend.models.service_modification import ServiceModification

service_modifications_bp = Blueprint('service_modifications', __name__)

# Dummy data function for demo purpose
def create_service_modification(user_id: int, service_type: str) -> ServiceModification:
    # Simulate creating service modification request
    return ServiceModification(modification_id=1, user_id=user_id, service_type=service_type, status="Pending")

def get_user_service_modifications(user_id: int) -> List[ServiceModification]:
    return [
        ServiceModification(modification_id=1, user_id=user_id, service_type='Upgrade Plan', status='Approved')
    ]

@service_modifications_bp.route('/service_modifications', methods=['GET', 'POST'])
def service_modifications():
    user_id = session.get('user_id')
    if not user_id:
        return "Access Denied", 403

    if request.method == 'POST':
        service_type = request.form['service_type']
        service_modification = create_service_modification(user_id, service_type)
        # Simulate saving to database
        
        return redirect(url_for('service_modifications.service_modifications'))
    
    service_modifications = get_user_service_modifications(user_id)
    return render_template('service_modifications.html', service_modifications=service_modifications)
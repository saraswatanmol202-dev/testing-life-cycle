# Epic Title: Approval and Processing Workflows

from flask import Blueprint, render_template, request, redirect, url_for, session
from typing import List

# Importing models
from backend.models.request import Request

request_processing_bp = Blueprint('request_processing', __name__)

# Dummy data function for demo purpose
def create_request(user_id: int, request_type: str) -> Request:
    # Simulate creating a request
    return Request(request_id=1, user_id=user_id, request_type=request_type, status="Pending")

def get_user_requests(user_id: int) -> List[Request]:
    return [
        Request(request_id=1, user_id=user_id, request_type='Account Opening', status='Approved'),
        Request(request_id=2, user_id=user_id, request_type='Service Modification', status='Pending')
    ]

def approve_request(request_id: int) -> None:
    # Simulate approving a request
    pass

def process_request(request_id: int) -> None:
    # Simulate processing a request
    pass

@request_processing_bp.route('/request_processing', methods=['GET', 'POST'])
def request_processing():
    user_id = session.get('user_id')
    if not user_id:
        return "Access Denied", 403

    if request.method == 'POST':
        request_type = request.form['request_type']
        new_request = create_request(user_id, request_type)
        # Simulate saving to database
        
        return redirect(url_for('request_processing.request_processing'))
    
    user_requests = get_user_requests(user_id)
    return render_template('request_processing.html', user_requests=user_requests)

@request_processing_bp.route('/request_processing/approve/<int:request_id>', methods=['POST'])
def approve(request_id: int):
    approve_request(request_id)
    process_request(request_id)
    # Simulate updating request status in the database
    
    return redirect(url_for('request_processing.request_processing'))
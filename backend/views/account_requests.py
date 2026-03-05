# Epic Title: Streamline Account Opening Requests

from flask import Blueprint, render_template, request, redirect, url_for, session
from typing import List

# Importing models
from backend.models.account_request import AccountRequest

account_requests_bp = Blueprint('account_requests', __name__)

# Dummy data function for demo purpose
def create_account_request(user_id: int, account_type: str) -> AccountRequest:
    # Simulate creating account request
    return AccountRequest(request_id=1, user_id=user_id, account_type=account_type, status="Pending")

def get_user_account_requests(user_id: int) -> List[AccountRequest]:
    return [
        AccountRequest(request_id=1, user_id=user_id, account_type='Savings', status='Approved')
    ]

@account_requests_bp.route('/account_requests', methods=['GET', 'POST'])
def account_requests():
    user_id = session.get('user_id')
    if not user_id:
        return "Access Denied", 403

    if request.method == 'POST':
        account_type = request.form['account_type']
        account_request = create_account_request(user_id, account_type)
        # Simulate saving to database
        
        return redirect(url_for('account_requests.account_requests'))
    
    account_requests = get_user_account_requests(user_id)
    return render_template('account_requests.html', account_requests=account_requests)
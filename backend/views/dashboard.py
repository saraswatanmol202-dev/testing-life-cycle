# Epic Title: Develop a User-Friendly Dashboard

from flask import Blueprint, render_template, session
from typing import List

# Importing models
from backend.models.account import Account
from backend.models.transaction import Transaction

dashboard_bp = Blueprint('dashboard', __name__)

# Dummy data function for demo purpose
def get_user_accounts(user_id: int) -> List[Account]:
    return [
        Account(1, user_id, 'Checking', 1500.00),
        Account(2, user_id, 'Savings', 2500.00)
    ]

def get_account_transactions(account_id: int) -> List[Transaction]:
    return [
        Transaction(1, account_id, -20.00, 'debit', datetime.now()),
        Transaction(2, account_id, 500.00, 'credit', datetime.now())
    ]

@dashboard_bp.route('/dashboard')
def dashboard():
    user_id = session.get('user_id')
    if not user_id:
        # Redirect to login or show access denied
        return "Access Denied", 403
    
    accounts = get_user_accounts(user_id)
    transactions = {account.account_id: get_account_transactions(account.account_id) for account in accounts}
    
    return render_template('dashboard.html', accounts=accounts, transactions=transactions)
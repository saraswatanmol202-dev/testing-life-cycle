# Epic Title: Overview of Financial Activities

from flask import Blueprint, render_template, session, request, redirect, url_for
from typing import List, Dict

# Importing models
from backend.models.account import Account
from backend.models.transaction import Transaction
from backend.models.widget import Widget

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

def get_user_widgets(user_id: int) -> List[Widget]:
    return [
        Widget(1, user_id, 'Weather'),
        Widget(2, user_id, 'Stock Ticker')
    ]

def summarize_financial_activity(accounts: List[Account], transactions: Dict[int, List[Transaction]]) -> Dict[str, float]:
    total_balance = sum(account.balance for account in accounts)
    total_transactions_amount = sum(txn.amount for txns in transactions.values() for txn in txns)
    return {
        "total_balance": total_balance,
        "total_transactions_amount": total_transactions_amount
    }

@dashboard_bp.route('/dashboard')
def dashboard():
    user_id = session.get('user_id')
    if not user_id:
        return "Access Denied", 403
    
    accounts = get_user_accounts(user_id)
    transactions = {account.account_id: get_account_transactions(account.account_id) for account in accounts}
    widgets = get_user_widgets(user_id)
    summary = summarize_financial_activity(accounts, transactions)
    
    return render_template('dashboard.html', accounts=accounts, transactions=transactions, widgets=widgets, summary=summary)

@dashboard_bp.route('/dashboard/add_widget', methods=['POST'])
def add_widget():
    user_id = session.get('user_id')
    if not user_id:
        return "Access Denied", 403

    widget_type = request.form.get('widget_type')
    # Simulate adding the widget to the database
    new_widget = Widget(widget_id=3, user_id=user_id, widget_type=widget_type)
    # Simulated: add new_widget to the user's list of widgets

    return redirect(url_for('dashboard.dashboard'))

@dashboard_bp.route('/dashboard/remove_widget/<int:widget_id>', methods=['POST'])
def remove_widget(widget_id: int):
    user_id = session.get('user_id')
    if not user_id:
        return "Access Denied", 403

    # Simulate removing the widget from the database
    # Simulated: remove the widget from the user's list of widgets

    return redirect(url_for('dashboard.dashboard'))
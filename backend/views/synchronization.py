# Epic Title: Data Synchronization Mechanisms

from flask import Blueprint, jsonify, session
from datetime import datetime
import requests
import logging

# Importing models
from backend.models.synchronization_log import SynchronizationLog

synchronization_bp = Blueprint('synchronization', __name__)

CORE_BANKING_SYSTEM_URL = "https://core-banking-system.example.com"

# Dummy function for demo purpose
def save_synchronization_log(sync_type: str, status: str, details: str) -> SynchronizationLog:
    # Simulate saving the synchronization log to the database
    return SynchronizationLog(sync_id=1, sync_type=sync_type, status=status, details=details, created_at=datetime.utcnow())

@synchronization_bp.route('/sync_data', methods=['GET'])
def sync_data():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "Access Denied"}), 403

    try:
        response = requests.get(f"{CORE_BANKING_SYSTEM_URL}/data")
        response.raise_for_status()
        data = response.json()
        status = "Successful"
    except Exception as e:
        logging.error(f"Error during data synchronization: {e}")
        data = {"error": str(e)}
        status = "Failed"

    # Save synchronization log
    save_synchronization_log(sync_type="fetch_data", status=status, details=str(data))

    return jsonify(data)
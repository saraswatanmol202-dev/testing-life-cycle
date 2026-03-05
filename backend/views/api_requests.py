# Epic Title: Develop Secure APIs

from flask import Blueprint, request, jsonify, session
from datetime import datetime
import requests  # For making HTTP requests to the core banking system
import logging

# Importing models
from backend.models.api_request import APIRequest

api_requests_bp = Blueprint('api_requests', __name__)

CORE_BANKING_SYSTEM_URL = "https://core-banking-system.example.com"

# Dummy data function for demo purpose
def save_api_request(user_id: int, endpoint: str, request_body: str, response_body: str, status: str) -> APIRequest:
    # Simulate saving the API request metadata to the database
    return APIRequest(request_id=1, user_id=user_id, endpoint=endpoint, request_body=request_body, response_body=response_body, status=status, created_at=datetime.utcnow())

@api_requests_bp.route('/api/v1/integration', methods=['POST'])
def api_integration():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "Access Denied"}), 403

    data = request.json
    endpoint = data.get('endpoint')
    request_body = data.get('request_body')

    # Make the request to the core banking system
    try:
        response = requests.post(f"{CORE_BANKING_SYSTEM_URL}/{endpoint}", json=request_body)
        response_body = response.json()
        status = "Success" if response.status_code == 200 else "Failed"
    except Exception as e:
        logging.error(f"Error making API request to core banking system: {e}")
        response_body = {"error": str(e)}
        status = "Failed"

    # Save API request info to "database"
    save_api_request(user_id, endpoint, request_body, response_body, status)

    return jsonify(response_body)
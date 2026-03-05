# Epic Title: Maintain Separate Database

from flask import Blueprint, request, jsonify, session
from datetime import datetime
import logging

# Importing models
from backend.models.local_data import LocalData
from backend.views.synchronization import sync_data  # Assuming sync_data can be used for fetching core banking data

local_data_bp = Blueprint('local_data', __name__)

# Dummy function for demo purpose
def save_local_data(user_id: int, data_type: str, content: str) -> LocalData:
    # Simulate saving local data to the database
    return LocalData(data_id=1, user_id=user_id, data_type=data_type, content=content, created_at=datetime.utcnow())

def fetch_local_data(user_id: int, data_type: str) -> LocalData:
    # Simulate fetching local data from the database
    return LocalData(data_id=1, user_id=user_id, data_type=data_type, content="Local database content", created_at=datetime.utcnow())

@local_data_bp.route('/data', methods=['GET'])
def get_data():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "Access Denied"}), 403

    data_type = request.args.get('type')
    if not data_type:
        return jsonify({"error": "Data type is required"}), 400

    try:
        local_data = fetch_local_data(user_id, data_type)
        core_data = sync_data().get_json()
        
        combined_data = {
            "local_data": local_data.content,
            "core_data": core_data
        }
        
        return jsonify(combined_data)
    except Exception as e:
        logging.error(f"Error fetching data: {e}")
        return jsonify({"error": str(e)}), 500

@local_data_bp.route('/data', methods=['POST'])
def save_data():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "Access Denied"}), 403

    data_type = request.json.get('data_type')
    content = request.json.get('content')
    if not data_type or not content:
        return jsonify({"error": "Data type and content are required"}), 400

    try:
        local_data = save_local_data(user_id, data_type, content)
        return jsonify({"message": "Data saved successfully", "data_id": local_data.data_id})
    except Exception as e:
        logging.error(f"Error saving data: {e}")
        return jsonify({"error": str(e)}), 500
# Epic Title: Maintain Interaction History

from flask import Blueprint, render_template, session
from typing import List

# Importing models
from backend.models.interaction_history import InteractionHistory

interaction_history_bp = Blueprint('interaction_history', __name__)

# Dummy data function for demo purpose
def get_user_interaction_history(user_id: int) -> List[InteractionHistory]:
    # Simulate retrieving interaction history from the database
    return [
        InteractionHistory(history_id=1, user_id=user_id, action="Logged in", timestamp=datetime.utcnow()),
        InteractionHistory(history_id=2, user_id=user_id, action="Submitted a request", timestamp=datetime.utcnow())
    ]

@interaction_history_bp.route('/interaction_history', methods=['GET'])
def interaction_history():
    user_id = session.get('user_id')
    if not user_id:
        return "Access Denied", 403

    history = get_user_interaction_history(user_id)
    return render_template('interaction_history.html', history=history)
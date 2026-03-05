# Epic Title: Save and Resume Incomplete Applications

from flask import Blueprint, request, session, jsonify, render_template, redirect, url_for
from datetime import datetime
from typing import List

# Importing models
from backend.models.application import Application

application_bp = Blueprint('application', __name__)

# Dummy data function for demo purpose
def get_user_applications(user_id: int) -> List[Application]:
    # Simulate retrieving applications from the database
    return [
        Application(application_id=1, user_id=user_id, content="Application Content 1", status="Incomplete", last_modified=datetime.utcnow()),
        Application(application_id=2, user_id=user_id, content="Application Content 2", status="Complete", last_modified=datetime.utcnow())
    ]

def save_application(user_id: int, content: str, status: str) -> Application:
    # Simulate saving the application to the database
    return Application(application_id=3, user_id=user_id, content=content, status=status, last_modified=datetime.utcnow())

@application_bp.route('/application', methods=['GET', 'POST'])
def manage_application():
    user_id = session.get('user_id')
    if not user_id:
        return "Access Denied", 403

    if request.method == 'POST':
        content = request.form.get('content')
        status = request.form.get('status')
        
        # Save application
        application = save_application(user_id, content, status)

        if status == "Complete":
            return redirect(url_for('application.application_success'))
        
        return redirect(url_for('application.manage_application'))

    applications = get_user_applications(user_id)
    return render_template('manage_application.html', applications=applications)

@application_bp.route('/application_success', methods=['GET'])
def application_success():
    return render_template('application_success.html')
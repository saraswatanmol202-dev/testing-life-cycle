# Epic Title: Document Upload Capability

import os
from flask import Blueprint, request, redirect, url_for, session, flash
from werkzeug.utils import secure_filename
from datetime import datetime

# Importing models
from backend.models.document import Document

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'doc', 'docx'}
UPLOAD_FOLDER = 'backend/static/uploads'

document_upload_bp = Blueprint('document_upload', __name__)

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_document(user_id: int, filename: str, upload_path: str) -> Document:
    # Simulate saving the document metadata to the database
    return Document(document_id=1, user_id=user_id, filename=filename, upload_path=upload_path, upload_date=datetime.utcnow())

@document_upload_bp.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        user_id = session.get('user_id')
        if not user_id:
            return "Access Denied", 403

        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(upload_path)

            # Save document info to "database"
            save_document(user_id, filename, upload_path)

            flash('File successfully uploaded')
            return redirect(url_for('document_upload.upload_file'))

    return 
    <!doctype html>
    <title>Upload Document</title>
    <h1>Upload Document</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
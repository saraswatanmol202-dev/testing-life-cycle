# Epic Title: Consistency Across Devices

from flask import Blueprint, render_template

consistency_bp = Blueprint('consistency', __name__)

@consistency_bp.route('/consistency')
def consistency():
    return render_template('consistency.html')
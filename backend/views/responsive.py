# Epic Title: Implement Adaptive Layouts

from flask import Blueprint, render_template

responsive_bp = Blueprint('responsive', __name__)

@responsive_bp.route('/responsive')
def responsive():
    return render_template('responsive.html')
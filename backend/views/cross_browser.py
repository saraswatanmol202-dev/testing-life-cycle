# Epic Title: Cross-Browser Compatibility

from flask import Blueprint, render_template

cross_browser_bp = Blueprint('cross_browser', __name__)

@cross_browser_bp.route('/cross_browser')
def cross_browser():
    return render_template('cross_browser.html')
from flask import Blueprint, render_template
about_bp = Blueprint('about_bp', __name__)

@about_bp.route('/about', methods=['GET'], strict_slashes=False)
def about():
    return render_template('about.html')
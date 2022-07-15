from flask import Blueprint, render_template
index_bp = Blueprint('index_bp', __name__)
about_bp = Blueprint('about_bp', __name__)

@index_bp.route('/', methods=['GET'], strict_slashes=False)
def index():
    return render_template('index.html')

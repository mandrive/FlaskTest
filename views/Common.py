from flask import Blueprint, render_template
from utils.utils import login_required

mod = Blueprint('Common', __name__)


@mod.route('/')
@login_required
def index():
    return render_template('index.html')


@mod.route('/unauthorized')
def unauthorized():
    return render_template('unauthorized.html')
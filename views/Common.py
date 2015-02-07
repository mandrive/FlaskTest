from flask import Blueprint, render_template
from utils.utils import login_required

mod = Blueprint('Common', __name__)


@mod.route('/')
@login_required
def index_path():
    return render_template('index.html')
from flask import Blueprint, render_template

mod = Blueprint('Common', __name__)


@mod.route('/')
def index_path():
    return render_template('index.html')
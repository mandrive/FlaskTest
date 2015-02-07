from flask import Blueprint
from utils.utils import templated, login_required, admin_only


mod = Blueprint('Admin', __name__)


@mod.route('/admin')
@templated('Admin/index.html')
@login_required
@admin_only
def admin():
    pass
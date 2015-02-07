from flask import Blueprint, render_template, request
from flask_login import login_user, logout_user, login_required
from werkzeug.utils import redirect

from models.LoginModel import LoginModel
from services.Services import UserService


mod = Blueprint('Login', __name__)


@mod.route('/login', methods=['GET', 'POST'])
def login_page():
    loginmodel = LoginModel()
    if loginmodel.validate_on_submit():
        if loginmodel.validateCredentials():
            user = UserService().getUserByUsername(loginmodel.Username.data)
            login_user(user)
            nextUrl = request.args.get('next', '')
            if nextUrl is not None:
                return redirect(nextUrl)
            return redirect('/')
        loginmodel.Username.errors.append('User does not exist in database!')
    return render_template('Login/login.html', form=loginmodel)


@mod.route('/logout')
def logout_page():
    logout_user()
    return redirect('/')
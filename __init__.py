import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template
from flask_login import LoginManager
from flask_restful import Api
from flask_wtf.csrf import CsrfProtect
from sqlalchemy import create_engine

import AppConfig
from RestResources.Resources import PostsList, Posts
from services.Services import UserService
from views import Login, Common, Post


app = Flask(__name__)

CsrfProtect(app)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# set the secret key.  keep this really secret:
app.secret_key = AppConfig.APPSECRETKEY


def register_mods():
    app.register_blueprint(Common.mod)
    app.register_blueprint(Login.mod)
    app.register_blueprint(Post.mod)


def create_db_engine():
    return create_engine(AppConfig.CONNECTIONSTRING, pool_recycle=3600, echo=True)


def build_db_engine():
    AppConfig.DBENGINE = create_db_engine()


def init_login():
    login_manager = LoginManager()
    login_manager.init_app(app)
    AppConfig.LOGINMANAGER = login_manager

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return UserService().getAll().filter_by(id=user_id).first()

    @login_manager.token_loader
    def get_user_token(user_id):
        return UserService().getAll().filter_by(id=user_id).first().get


def init_logger():
    handler = RotatingFileHandler('FlaskTest.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)


def register_rest_api():
    return Api(app)


def register_rest_resources():
    api.add_resource(PostsList, '/api/posts')
    api.add_resource(Posts, '/api/posts/<string:post_id>')


register_mods()
api = register_rest_api()
register_rest_resources()
build_db_engine()
init_login()
init_logger()

app.run(AppConfig.APPHOST, AppConfig.APPPORT)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
import os
# from flask import Bootstrap

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '$hj$!sh$jh$dja@h kj#s!!Zj@dh#js&'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    bcrypt = Bcrypt(app)

    from .views_py_file.views import views
    from .auth_py_file.auth import auth
    from .user_py_file.userlist import userlist
    from .chart_dashboard_py_file.req_dashboard import req_dashboard
    from .add_edit_requirement_py_file.add_requirement import add_requirement

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(userlist, url_prefix='/')
    app.register_blueprint(req_dashboard, url_prefix='/')
    app.register_blueprint(add_requirement, url_prefix='/')

    from .models_py_file.models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "backup.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hello102jodvkdnj'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = ' postgres://etdkimmgwgaqbb:4d7758cfc3ad6dbec865770a5f9d2290b6b3453f2eb6efe57c49977dc305a9d1@ec2-3-213-66-35.compute-1.amazonaws.com:5432/d9ll7h1dlputgs'
    db.init_app(app)

    from website.views import views
    from website.auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from website.models import User, BlogPost

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

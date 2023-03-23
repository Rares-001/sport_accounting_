from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_name)

    db.init_app(app)
    login_manager.init_app(app)

    from app.routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from app.routes.home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app

from app import models

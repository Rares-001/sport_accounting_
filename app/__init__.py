from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/sport_accounting'

    if config:
        app.config.from_object(config)

    db.init_app(app)
    login_manager.init_app(app)

    from .routes.home import home_bp
    app.register_blueprint(home_bp)

    from .routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    # Fix for 403 error: add the following lines
    CORS(app)

    return app

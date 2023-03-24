from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_bootstrap import Bootstrap
import os

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
bootstrap = Bootstrap()

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bootstrap.init_app(app)

    from .models.user import User
    from .models.sport import Sport
    from .models.payment import Payment

    @app.route('/')
    def index():
        return render_template('index.html')

    from .api import api_bp
    app.register_blueprint(api_bp)

    return app

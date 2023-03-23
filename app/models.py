from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_required, current_user
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/sport_accounting'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)
login_manager = LoginManager(app)
login_manager.login_view = 'admin.login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'warning'

# Import models and views
from .models import User, Post
from .admin import admin_blueprint
from .main import main_blueprint

# Register blueprints
app.register_blueprint(admin_blueprint)
app.register_blueprint(main_blueprint)

# Create admin user if it doesn't exist
@app.before_first_request
def create_admin_user():
    admin = User.query.filter_by(email='admin@example.com').first()
    if not admin:
        admin = User(email='admin@example.com', password='your-password-here')
        db.session.add(admin)
        db.session.commit()

# Initialize login manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    app.run()


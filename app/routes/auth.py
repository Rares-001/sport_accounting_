from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from app.models.user import User
from app.forms.auth import LoginForm, RegisterForm
from app import db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/register', methods=['POST'])
def register():
    form = RegistrationForm(request.form)
    if form.validate():
        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        user = create_user(email=email, password=password, first_name=first_name, last_name=last_name)

        return jsonify({
            'success': True,
            'message': 'Registration successful.'
        })
    else:
        return jsonify({
            'success': False,
            'message': 'Registration failed.',
            'errors': form.errors
        })


@auth_bp.route('/login', methods=['POST'])
def login():
    form = LoginForm(request.form)
    if form.validate():
        email = form.email.data
        password = form.password.data

        user = authenticate_user(email=email, password=password)

        if user:
            token = generate_token(user.id)
            return jsonify({
                'success': True,
                'message': 'Login successful.',
                'token': token
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Invalid email or password.'
            })
    else:
        return jsonify({
            'success': False,
            'message': 'Login failed.',
            'errors': form.errors
        })

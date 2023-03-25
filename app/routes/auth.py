from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required
from app import db
from app.forms import LoginForm, RegistrationForm
from app.utils import create_user, authenticate_user

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


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = authenticate_user(email=email, password=password)

        if user:
            login_user(user)
            flash('You have been logged in!', 'success')
            return redirect(url_for('home.index'))
        else:
            flash('Invalid email or password.', 'error')
            return redirect(url_for('auth.login'))

    return render_template('login.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out!', 'success')
    return redirect(url_for('home.index'))

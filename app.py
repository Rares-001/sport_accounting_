from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from models.customer import Customer
from models.club import Club
from models.bank import Bank
from database import db as db_instance
from sqlalchemy import text
import pymongo
from pymongo import MongoClient
import certifi
import ssl


app = Flask(__name__)
app.config.from_object('config')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/sport_accounting'

app.secret_key = 'quintor-project-accounting-sports-a1b2c3'

login_manager = LoginManager()
login_manager.init_app(app)

db_instance.init_app(app)

client = pymongo.MongoClient("mongodb+srv://Rares:admin@cluster0.y9osbya.mongodb.net/?retryWrites=true&w=majorit", tlsCAFile=certifi.where())
db = client.get_database("test")

MT940_COLLECTION = "MTFiles_records"
collection = db[MT940_COLLECTION]

ca = certifi.where()


#---------------------------------------

@app.route('/')
def index():
    if 'customer_id' in session:
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('login'))


#---------------------------------------

@login_manager.user_loader
def load_user(user_id):
    return Customer.query.get(int(user_id))

#---------------------------------------

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        address = request.form['address']
        clubid = request.form['club']

        hashed_password = generate_password_hash(password, method='sha256')

        new_customer = Customer(
            username=username,
            password_=hashed_password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            address=address,
            clubid=clubid
        )

        db_instance.session.add(new_customer)
        db_instance.session.commit()

        return redirect(url_for('login'))

    clubs = Club.query.all()
    return render_template('register.html', clubs=clubs)

#---------------------------------------

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        customer = Customer.query.filter_by(username=username).first()

        if customer is None:
            flash('Invalid username')
            return redirect(url_for('login'))

        if not check_password_hash(customer.password_, password):
            flash('Invalid password')
            return redirect(url_for('login'))

        session['customer_id'] = customer.customer_id

        login_user(customer)
        return redirect(url_for('dashboard'))

    return render_template('login.html')

#---------------------------------------

@app.route('/dashboard')
@login_required
def dashboard():
    # Check if customer_id exists in session
    if 'customer_id' not in session:
        flash('Please login to access your dashboard.', 'error')
        return redirect(url_for('login'))

    # Retrieve customer information from Postgres
    customer = Customer.query.filter_by(customer_id=session['customer_id']).first()

    # Retrieve MT940 file content from MongoDB
    mt940_document = collection.find_one()

    if mt940_document is None:
        mt940_content = ''
    else:
        mt940_content = mt940_document.get('file_content', '')

    # Pass customer and MT940 content to dashboard template
    return render_template('dashboard.html', customer=customer, mt940_content=mt940_content)


#---------------------------------------

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))




#test to insert data to the data base
@app.route("/test")
def test():
    return "Connected to the data base!"

if __name__ == '__main__':
    app.debug = True
    with app.app_context():
        db_instance.create_all()
    app.run()

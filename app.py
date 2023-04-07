import json
import pprint

import certifi
import mt940
import pymongo
import xmltodict
from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_login import LoginManager, login_user, current_user, login_required
from flask_table import Table, Col
from flask_wtf import FlaskForm
from sqlalchemy import create_engine
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired

from database import db as db_instance
from models.club import Club
from models.customer import Customer
from models.admin import Admin

app = Flask(__name__)
app.config.from_object('config')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/sport_accounting'

app.secret_key = 'quintor-project-accounting-sports-a1b2c3'

login_manager = LoginManager()
login_manager.init_app(app)

db_instance.init_app(app)

client = pymongo.MongoClient("mongodb+srv://Terry:PA$$W0RD@cluster0.y9osbya.mongodb.net/?retryWrites=true&w=majority",
                             tlsCAFile = certifi.where())

db = client.get_database("MT940_id")

MT940_COLLECTION = "MTFiles_records"

records = db.MTFiles_records

collection = db[MT940_COLLECTION]

RawFile = records.find()

ALLOWED_EXTENSIONS = {'txt', 'sta'}

mt940file = "mt940test.sta"

ca = certifi.where()

engine = create_engine('postgresql://postgres:Tex1game!@localhost/postgresDB')


# ---------------------------------------

class UploadFileForm(FlaskForm):
    file = FileField("File", validators = [InputRequired()])
    submit = SubmitField("Upload File")


# ----------------------------------------

@app.route('/')
def index():
    if current_user.is_authenticated:
        # User is logged in, render index template
        return render_template('index.html')
    # User is not authenticated, render index template anyway
    return render_template('index.html')


# ---------------------------------------

@login_manager.user_loader
def load_user(user_id):
    return Customer.query.get(int(user_id))


# ---------------------------------------

@app.route('/register', methods = ['GET', 'POST'])
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

        hashed_password = generate_password_hash(password, method = 'sha256')

        new_customer = Customer(
            username = username,
            password_ = hashed_password,
            first_name = first_name,
            last_name = last_name,
            email = email,
            phone_number = phone_number,
            address = address,
            clubid = clubid
        )

        db_instance.session.add(new_customer)
        db_instance.session.commit()

        return redirect(url_for('login'))

    clubs = Club.query.all()
    return render_template('register.html', clubs = clubs)


# ---------------------------------------

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the user is a Customer
        customer = Customer.query.filter_by(username=username).first()
        if customer is not None and check_password_hash(customer.password_, password):
            session['customer_id'] = customer.customer_id
            login_user(customer)
            return redirect(url_for('dashboard'))

        # Check if the user is an Admin
        admin = Admin.query.filter_by(email=username).first()
        if admin is not None and check_password_hash(admin.password_, password):
            session['admin_id'] = admin.adminid
            return redirect(url_for('admin'))

        flash('Invalid username or password')
        return redirect(url_for('login'))

    return render_template('login.html')



# ---------------------------------------

@app.route('/dashboard')
@login_required
def dashboard():
    # Check if customer_id exists in session
    if 'customer_id' not in session:
        flash('Please login to access your dashboard.', 'error')
        return redirect(url_for('login'))

    # Retrieve customer information from Postgres
    customer = Customer.query.filter_by(customer_id = session['customer_id']).first()

    # Retrieve MT940 file content from MongoDB
    mt940_document = collection.find_one()

    if mt940_document is None:
        mt940_content = ''
    else:
        mt940_content = mt940_document.get('file_content', '')

    # Pass customer and MT940 content to dashboard template
    return render_template('dashboard.html', customer = customer, mt940_content = mt940_content)


# ---------------------------------------

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route("/test")
def test():
    return "Connected to the data base!"


# ---------------------------------------
@app.route("/adminHome.html", methods = ["GET", "POST"])
# This is the Home page for the treaser
@app.route('/adminHome.html')
def admin():
    return render_template('adminHome.html')


# ---------------------------------------
# This is the upload page/parcel to upload the MT940 files

@app.route('/upload.html', methods = ["GET", "POST"])
def upload_files():
    if request.method == 'POST':
        file = request.files['file']
        transactions = mt940.parse(file)

        print('Transactions:')
        print(transactions)
        pprint.pprint(transactions.data)

        for transaction in transactions:
            print('Transaction: ', transaction)
            pprint.pprint(transaction.data)
            mt940.tags.BalanceBase.scope = mt940.models.Transaction

        transactions = mt940.models.Transactions(processors = dict(
            pre_statement = [
                mt940.processors.add_currency_pre_processor('EUR'),
            ],
        ))
        transactions = mt940.parse(file)

        # Use the built-in json module to convert the transaction object to a JSON string
        translated = json.dumps(transactions, indent = 4)

        FinalVersion = json.loads(translated)
        print(translated)
        records.insert_one(FinalVersion)
    return render_template("upload.html")


# ---------------------------------------
# creating the most important columns in the database to show to the admin

class Results(Table):
    id = Col('transactionid', show = True)
    bankid = Col('bankid')
    user = Col('customerid')
    date = Col('date')
    amount = Col('amount')
    currency = Col('currency')
    status = Col('status')
    transactionDetail = Col('transaction_detail')


# ---------------------------------------
# choosing which table to get information
def get_results():
    conn = engine.connect()
    results = conn.execute("SELECT * FROM transaction").fetchall()
    conn.close()
    return results


# ---------------------------------------
# This is the transaction page which will show you the Raw transactions

@app.route('/transactions.html')
def transactions():
    results = get_results()
    table = Results(results)
    return render_template('transactions.html', table = table)


# ---------------------------------------
# This is the upload of the xml file
@app.route('/xmlUpload.html', methods = ["GET", "POST"])
def xmlUpload():
    if request.method == 'POST':
        file = request.files['fileXml']
        transactions = mt940.parse(file)

        print('Transactions:')
        print(transactions)
        pprint.pprint(transactions.data)

        for transaction in transactions:
            print('Transaction: ', transaction)
            pprint.pprint(transaction.data)
            mt940.tags.BalanceBase.scope = mt940.models.Transaction

        transactions = mt940.models.Transactions(processors = dict(
            pre_statement = [
                mt940.processors.add_currency_pre_processor('EUR'),
            ],
        ))
        transactions = mt940.parse(file)
        translated = json.dumps(transaction, indent = 4, cls = mt940.JSONEncoder)
        data = json.loads(translated)
        xml_string = xmltodict.unparse({'mt940': data}, pretty = False)

        with open('mt940.xml', 'w') as f:
            f.write(xml_string)

    return render_template('xmlUpload.html')


# ---------------------------------------


if __name__ == '__main__':
    app.debug = True
    with app.app_context():
        db_instance.create_all()
    app.run()

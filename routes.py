from flask import Flask ,render_template,request
from flask_table import Table, Col
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
import mt940
import pprint
import json
import xmltodict
from pymongo import MongoClient
import psycopg2





# Connectiong to the NoSql Database
client = MongoClient("mongodb+srv://Terry:PA$$W0RD@cluster0.y9osbya.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('MT940_id')
records = db.MTFiles_records
RawFile = records.find()

ALLOWED_EXTENSIONS = {'txt', 'sta'}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'
mt940file = "mt940test.sta"

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route("/",methods=["GET","POST"])
#This is the Home page for the treaser
@app.route('/adminHome.html')
def admin():
   return render_template('adminHome.html')

# This is the upload page/parcel to upload the MT940 files

@app.route('/upload.html', methods=["GET","POST"])
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

        transactions = mt940.models.Transactions(processors=dict(
            pre_statement=[
                mt940.processors.add_currency_pre_processor('EUR'),
            ],
        )) 
        transactions = mt940.parse(file)
        translated = json.dumps(transaction, indent=4, cls=mt940.JSONEncoder)
        FinalVersion = json.loads(translated)
        print(translated)
        records.insert_one(FinalVersion)
    return render_template("upload.html")


# creating the most important columns in the database to show to the admin panel
class Results(Table):
    id = Col('transactionid', show=True)
    bankid = Col('bankid')
    user = Col('customerid')
    date = Col('date')
    amount = Col('amount')
    currency = Col('currency')
    status = Col('status')
    transactionDetail = Col('transaction_detail')

#choosing which table to get information
def get_results():
    conn = psycopg2.connect(host="localhost",database="postgresDB",user="postgres",password="Tex1game!")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transaction")
    results = cursor.fetchall()
    return results
       
#This is the transaction page which will show you the Raw transactions
@app.route('/transactions.html')
def transactions():
                results = get_results()
                table = Results(results)
                return render_template('transactions.html', table=table)

#This is the upload of the xml file 
@app.route('/xmlUpload.html', methods=["GET","POST"])
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

        transactions = mt940.models.Transactions(processors=dict(
            pre_statement=[
                mt940.processors.add_currency_pre_processor('EUR'),
            ],
        )) 
        transactions = mt940.parse(file)
        translated = json.dumps(transaction, indent=4, cls=mt940.JSONEncoder)
        data = json.loads(translated)
        xml_string = xmltodict.unparse({'mt940': data}, pretty=False)

        with open('mt940.xml', 'w') as f:
            f.write(xml_string)
            
    return render_template('xmlUpload.html')
        
if __name__ == '__main__':
    app.run(debug=True)



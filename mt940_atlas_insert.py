import mt940
import json
from pymongo import MongoClient

client = MongoClient("mongodb+srv://Terry:PA$$W0RD@cluster0.y9osbya.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('MT940_id')
records = db.MTFiles_records

transactions = mt940.parse('mt940test.sta')

for transaction in transactions:
    # Convert each transaction to a dictionary
    transaction_dict = {
        'date': transaction.date.strftime('%Y-%m-%d'),
        'amount': str(transaction.amount),
        'currency': transaction.currency,
        'description': transaction.description,
        'reference': transaction.reference,
        'account': transaction.account,
        'contra_account': transaction.contra_account,
        'bank_code': transaction.bank_code,
        'customer_reference': transaction.customer_reference,
        'extra_details': transaction.extra_details,
    }
    
    # Insert the transaction into MongoDB
    records.insert_one(transaction_dict)


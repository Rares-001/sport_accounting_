import pymongo
import psycopg2
from sqlalchemy import create_engine

# Connect to MongoDB Atlas
MONGO_CONNECTION_STRING = "mongodb+srv://%3CRares%3E:%3Cadmin%3E@cluster0.y9osbya.mongodb.net/?retryWrites=true&w=majority"

mongo_client = pymongo.MongoClient(MONGO_CONNECTION_STRING, ssl=True)

mongo_db = mongo_client["MT940_id"]

mongo_collection = mongo_db["MTFiles_records"]


# Connect to PostgreSQL
postgres_uri = 'postgresql://postgres:admin@localhost:5432/sport_accounting'
engine = create_engine(postgres_uri)

# Retrieve data from MongoDB and insert into PostgreSQL
for mt940_doc in mongo_collection.find():
    amount = mt940_doc['amount']['amount']
    currency = mt940_doc['amount']['currency']
    customer_reference = mt940_doc['customer_reference']
    bank_reference = mt940_doc['bank_reference']
    transaction_details = mt940_doc['transaction_details']
    final_closing_balance = mt940_doc['final_closing_balance']['amount']['amount']
    available_balance = mt940_doc['available_balance']['amount']['amount']
    forward_available_balance = mt940_doc['forward_available_balance']['amount']['amount']

    with engine.connect() as conn:
        conn.execute("""
            INSERT INTO public.mt940_file (amount, currency, customer_reference, bank_reference, transaction_details, final_closing_balance, available_balance, forward_available_balance)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
            (amount, currency, customer_reference, bank_reference, transaction_details, final_closing_balance, available_balance, forward_available_balance))



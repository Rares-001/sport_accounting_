import pymongo
import pika
from sqlalchemy import create_engine

# Connect to MongoDB Atlas
MONGO_CONNECTION_STRING = "mongodb+srv://%3CRares%3E:%3Cadmin%3E@cluster0.y9osbya.mongodb.net/?retryWrites=true&w=majority"

mongo_client = pymongo.MongoClient(MONGO_CONNECTION_STRING, ssl=True)

mongo_db = mongo_client["MT940_id"]

mongo_collection = mongo_db["MTFiles_records"]


# Connect to PostgreSQL
postgres_uri = 'postgresql://postgres:admin@localhost:5432/sport_accounting'
engine = create_engine(postgres_uri)

# Set up RabbitMQ connection
rabbitmq_uri = 'amqp://guest:guest@localhost:5672/'
connection = pika.BlockingConnection(pika.URLParameters(rabbitmq_uri))
channel = connection.channel()
channel.queue_declare(queue='mt940_updates')


# Define callback function to handle incoming messages
def callback(ch, method, properties, body):
    # Extract relevant information from message
    mt940_doc = pymongo.collection.Collection.decode(body)
    amount = mt940_doc['amount']['amount']
    currency = mt940_doc['amount']['currency']
    customer_reference = mt940_doc['customer_reference']
    bank_reference = mt940_doc['bank_reference']
    transaction_details = mt940_doc['transaction_details']
    final_closing_balance = mt940_doc['final_closing_balance']['amount']['amount']
    available_balance = mt940_doc['available_balance']['amount']['amount']
    forward_available_balance = mt940_doc['forward_available_balance']['amount']['amount']

    # Insert into PostgreSQL database
    with engine.connect() as conn:
        conn.execute("""
            INSERT INTO public.mt940_file (amount, currency, customer_reference, bank_reference, transaction_details, final_closing_balance, available_balance, forward_available_balance)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
            (amount, currency, customer_reference, bank_reference, transaction_details, final_closing_balance, available_balance, forward_available_balance))
    print("Message processed:", body)


# Create a change stream in MongoDB
change_stream = mongo_collection.watch()

# Listen for changes in the change stream
for change in change_stream:
    # Send change document as message to RabbitMQ
    channel.basic_publish(exchange='', routing_key='mt940_updates', body=pymongo.collection.Collection.encode(change['fullDocument']))
    print("Message sent to RabbitMQ:", change['fullDocument'])

from datetime import date
from decimal import Decimal
from app import db

class Transaction(db.Model):
    __tablename__ = 'transaction'
    transaction_id = db.Column(db.Integer, primary_key=True, nullable=False)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    currency = db.Column(db.String(10), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('transaction_type.type_id'), nullable=False)
    customer_info = db.Column(db.String(255), nullable=True)
    bank_info = db.Column(db.String(255), nullable=True)
    guess_entry_date = db.Column(db.Date, nullable=True)
    transaction_detail = db.Column(db.String(255), nullable=True)
    amount_available = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    forward_balance = db.Column(db.Numeric(10, 2), nullable=False)

    def __init__(self, date, description, amount, currency, type_id, amount_available, status, forward_balance, customer_info=None, bank_info=None, guess_entry_date=None, transaction_detail=None):
        self.date = date
        self.description = description
        self.amount = Decimal(amount)
        self.currency = currency
        self.type_id = type_id
        self.customer_info = customer_info
        self.bank_info = bank_info
        self.guess_entry_date = guess_entry_date
        self.transaction_detail = transaction_detail
        self.amount_available = Decimal(amount_available)
        self.status = status
        self.forward_balance = Decimal(forward_balance)


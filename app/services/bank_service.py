from typing import List
from models import Transaction
from db import session

def get_transactions() -> List[Transaction]:
    return session.query(Transaction).all()

def get_transaction_by_id(transaction_id: int) -> Transaction:
    return session.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()

def add_transaction(transaction: Transaction) -> Transaction:
    session.add(transaction)
    session.commit()
    return transaction

def update_transaction(transaction_id: int, updated_fields: dict) -> Transaction:
    transaction = session.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
    for key, value in updated_fields.items():
        setattr(transaction, key, value)
    session.commit()
    return transaction

def delete_transaction(transaction_id: int) -> None:
    session.query(Transaction).filter(Transaction.transaction_id == transaction_id).delete()
    session.commit()


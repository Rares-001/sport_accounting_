from typing import List
from datetime import datetime
from sqlalchemy.orm import Session
from models.transaction import Transaction
from models.transaction_type import TransactionType


class TransactionService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_transactions(self) -> List[Transaction]:
        return self.db_session.query(Transaction).all()

    def create_transaction(self, date: datetime, description: str, amount: float,
                            currency: str, type_id: int, customer_info: str,
                            bank_info: str, guess_entry_date: datetime,
                            transaction_detail: str, amount_available: float,
                            status: str, forward_balance: float) -> Transaction:
        transaction = Transaction(date=date, description=description, amount=amount,
                                   currency=currency, type_id=type_id, customer_info=customer_info,
                                   bank_info=bank_info, guess_entry_date=guess_entry_date,
                                   transaction_detail=transaction_detail, amount_available=amount_available,
                                   status=status, forward_balance=forward_balance)
        self.db_session.add(transaction)
        self.db_session.commit()
        return transaction

    def get_transaction_types(self) -> List[TransactionType]:
        transaction_types = self.db_session.query(TransactionType).all()
        return transaction_types

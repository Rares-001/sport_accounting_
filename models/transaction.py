from sqlalchemy.orm import relationship

from database import db
from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Transaction(Base):
    __tablename__ = 'transaction'

    transactionid = Column(Integer, primary_key = True)
    moduleid = Column(Integer, nullable = False)
    bankid = Column(Integer, nullable = False)
    customerid = Column(Integer, nullable = False)
    date = Column(Date, nullable = False)
    description = Column(String(255), nullable = False)
    amount = Column(Numeric(10, 2), nullable = False)
    currency = Column(String(10), nullable = False)
    customer_info = Column(String(255), nullable = False)
    bank_info = Column(String(255), nullable = False)
    guess_entry_date = Column(Date, nullable = False)
    transaction_detail = Column(String(255), nullable = False)
    amount_available = Column(Numeric(10, 2), nullable = False)
    status = Column(String(20), nullable = False)
    forward_balance = Column(Numeric(10, 2), nullable = False)
    bank = relationship('Bank', backref = 'transactions')
    customer = relationship('Customer', backref = 'transactions')
    module = relationship('AccountingModule', backref = 'transactions')
    bankid_fkey = ForeignKey('bank.bankid')
    customerid_fkey = ForeignKey('customer.customer_id')
    moduleid_fkey = ForeignKey('accounting_module.moduleid')

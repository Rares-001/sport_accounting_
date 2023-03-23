from app import db

class TransactionType(db.Model):
    __tablename__ = 'transaction_types'
    type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)


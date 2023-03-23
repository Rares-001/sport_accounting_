from app import db

class Bank(db.Model):
    __tablename__ = 'bank'

    bank_id = db.Column(db.Integer, primary_key=True, nullable=False)
    bank_name = db.Column(db.String(255), nullable=False)
    bank_code = db.Column(db.String(10), nullable=False, unique=True)
    bic = db.Column(db.String(11), nullable=False, unique=True)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    website = db.Column(db.String(255), nullable=False)


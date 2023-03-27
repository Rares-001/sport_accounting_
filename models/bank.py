from database import db

class Bank(db.Model):
    __tablename__ = 'bank'
    bankid = db.Column(db.Integer, primary_key=True, server_default=db.text("nextval('bank_bankid_seq'::regclass)"))
    bank_name = db.Column(db.String(255), nullable=False)
    banklocation = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f"<Bank {self.bank_name}>"


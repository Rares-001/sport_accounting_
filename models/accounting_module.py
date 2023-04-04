from app import db

class AccountingModule(db.Model):
    __tablename__ = 'accounting_module'
    moduleid = db.Column(db.Integer, primary_key=True)
    module_name = db.Column(db.String(50), nullable=False)

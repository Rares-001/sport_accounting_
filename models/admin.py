from database import db

class Admin(db.Model):
    __tablename__ = 'admin'
    
    adminid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password_ = db.Column(db.String(255), nullable=False)

# app/models/customer.py

from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager
from flask_login import UserMixin


class Customer(db.Model, UserMixin):
    __tablename__ = 'customer'

    customerid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, index=True)
    password_hash = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    phone_number = db.Column(db.String(255))
    address = db.Column(db.String(255))
    clubid = db.Column(db.Integer, db.ForeignKey('club.clubid'), nullable=False)

    club = db.relationship('Club', backref='customers')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Customer %r>' % self.username


@login_manager.user_loader
def load_customer(customer_id):
    return Customer.query.get(int(customer_id))

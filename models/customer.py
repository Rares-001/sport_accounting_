from flask_login import UserMixin

from database import db as db_instance


class CustomMeta(type(db_instance.Model), type(UserMixin)):
    pass


class Customer(db_instance.Model, UserMixin, metaclass = CustomMeta):
    __tablename__ = 'customer'
    customer_id = db_instance.Column(db_instance.Integer, primary_key = True)
    username = db_instance.Column(db_instance.String(50), unique = True, nullable = False)
    password_ = db_instance.Column(db_instance.String(100), nullable = False)
    first_name = db_instance.Column(db_instance.String(50), nullable = False)
    last_name = db_instance.Column(db_instance.String(50), nullable = False)
    email = db_instance.Column(db_instance.String(100), nullable = False)
    phone_number = db_instance.Column(db_instance.String(20), nullable = False)
    address = db_instance.Column(db_instance.String(200), nullable = False)
    clubid = db_instance.Column(db_instance.Integer, db_instance.ForeignKey('club.clubid'), nullable = False)
    club = db_instance.relationship('Club', backref = db_instance.backref('customers', lazy = True))

    def get_id(self):
        return str(self.customer_id)

    def __repr__(self):
        return f"<Customer {self.username}>"

    def __init__(self, username, password_, first_name, last_name, email, phone_number, address, clubid):
        self.username = username
        self.password_ = password_
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.clubid = clubid

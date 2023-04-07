from database import db


class Club(db.Model):
    __tablename__ = 'club'
    clubid = db.Column(db.Integer, primary_key = True)
    clubname = db.Column(db.String(50), nullable = False)
    club_address = db.Column(db.String(100), nullable = False)
    club_city = db.Column(db.String(50), nullable = False)
    club_phone = db.Column(db.String(20), nullable = False)
    club_email = db.Column(db.String(50), nullable = False)
    bankid = db.Column(db.Integer, db.ForeignKey('bank.bankid'), nullable = False)
    bank = db.relationship('Bank', backref = db.backref('clubs', lazy = True))

    def __repr__(self):
        return f"<Club {self.clubname}>"

    def __init__(self, clubname, club_address, club_city, club_phone, club_email, bankid):
        self.clubname = clubname
        self.club_address = club_address
        self.club_city = club_city
        self.club_phone = club_phone
        self.club_email = club_email
        self.bankid = bankid

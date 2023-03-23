from models.club import Club
from db import db_session


def get_clubs():
    with db_session() as session:
        clubs = session.query(Club).all()
        return [club.to_dict() for club in clubs]


def get_club_by_id(club_id):
    with db_session() as session:
        club = session.query(Club).filter_by(club_id=club_id).first()
        return club.to_dict() if club else None


def create_club(name, description):
    with db_session() as session:
        club = Club(name=name, description=description)
        session.add(club)
        session.commit()
        return club.to_dict()


def update_club(club_id, name=None, description=None):
    with db_session() as session:
        club = session.query(Club).filter_by(club_id=club_id).first()
        if club:
            if name:
                club.name = name
            if description:
                club.description = description
            session.commit()
            return club.to_dict()
        else:
            return None


def delete_club(club_id):
    with db_session() as session:
        club = session.query(Club).filter_by(club_id=club_id).first()
        if club:
            session.delete(club)
            session.commit()
            return club.to_dict()
        else:
            return None


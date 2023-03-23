from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

from models import db
from models.club import Club

club_blueprint = Blueprint('club', __name__, url_prefix='/clubs')


@club_blueprint.route('/', methods=['POST'])
def create_club():
    data = request.get_json()
    club = Club(name=data['name'], city=data['city'])

    try:
        db.session.add(club)
        db.session.commit()
        return jsonify({'message': 'Club created successfully.'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Club already exists.'}), 409


@club_blueprint.route('/', methods=['GET'])
def get_all_clubs():
    clubs = Club.query.all()
    return jsonify([club.to_dict() for club in clubs]), 200


@club_blueprint.route('/<int:club_id>', methods=['GET'])
def get_club(club_id):
    club = Club.query.filter_by(club_id=club_id).first()
    if club is None:
        return jsonify({'error': 'Club not found.'}), 404
    return jsonify(club.to_dict()), 200


@club_blueprint.route('/<int:club_id>', methods=['PUT'])
def update_club(club_id):
    data = request.get_json()
    club = Club.query.filter_by(club_id=club_id).first()
    if club is None:
        return jsonify({'error': 'Club not found.'}), 404

    club.name = data['name']
    club.city = data['city']
    try:
        db.session.commit()
        return jsonify({'message': 'Club updated successfully.'}), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Club already exists.'}), 409


@club_blueprint.route('/<int:club_id>', methods=['DELETE'])
def delete_club(club_id):
    club = Club.query.filter_by(club_id=club_id).first()
    if club is None:
        return jsonify({'error': 'Club not found.'}), 404

    db.session.delete(club)
    db.session.commit()
    return jsonify({'message': 'Club deleted successfully.'}), 200


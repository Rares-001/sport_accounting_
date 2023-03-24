from flask import Blueprint, jsonify, request
from ..models.bank import Bank

bank_bp = Blueprint('bank', __name__, url_prefix='/banks')


@bank_bp.route('/', methods=['GET'])
def get_all_banks():
    """
    Return a list of all banks in the database.
    """
    banks = Bank.query.all()
    return jsonify([bank.serialize() for bank in banks]), 200


@bank_bp.route('/', methods=['POST'])
def create_bank():
    """
    Create a new bank record in the database.
    """
    bank_data = request.get_json()
    bank = Bank(**bank_data)
    bank.save()
    return jsonify(bank.serialize()), 201


@bank_bp.route('/<int:bank_id>', methods=['GET'])
def get_bank(bank_id):
    """
    Return a specific bank record based on its ID.
    """
    bank = Bank.query.get(bank_id)
    if bank:
        return jsonify(bank.serialize()), 200
    else:
        return jsonify({'message': 'Bank not found.'}), 404


@bank_bp.route('/<int:bank_id>', methods=['PUT'])
def update_bank(bank_id):
    """
    Update a specific bank record based on its ID.
    """
    bank_data = request.get_json()
    bank = Bank.query.get(bank_id)
    if bank:
        bank.update(**bank_data)
        return jsonify(bank.serialize()), 200
    else:
        return jsonify({'message': 'Bank not found.'}), 404


@bank_bp.route('/<int:bank_id>', methods=['DELETE'])
def delete_bank(bank_id):
    """
    Delete a specific bank record based on its ID.
    """
    bank = Bank.query.get(bank_id)
    if bank:
        bank.delete()
        return jsonify({'message': 'Bank deleted successfully.'}), 200
    else:
        return jsonify({'message': 'Bank not found.'}), 404


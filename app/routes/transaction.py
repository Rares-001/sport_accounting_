from flask import Blueprint, jsonify, request
from models.transaction import Transaction

transaction_bp = Blueprint('transaction', __name__)

@transaction_bp.route('/transactions')
def get_transactions():
    transactions = Transaction.query.all()
    return jsonify(transactions=[t.serialize() for t in transactions])

@transaction_bp.route('/transaction/<int:id>')
def get_transaction(id):
    transaction = Transaction.query.get(id)
    if not transaction:
        return jsonify(error="Transaction not found"), 404
    return jsonify(transaction.serialize())

@transaction_bp.route('/transaction', methods=['POST'])
def create_transaction():
    data = request.get_json()
    transaction = Transaction(date=data['date'],
                              description=data['description'],
                              amount=data['amount'],
                              currency=data['currency'],
                              type_id=data['type_id'],
                              customer_info=data.get('customer_info'),
                              bank_info=data.get('bank_info'),
                              guess_entry_date=data.get('guess_entry_date'),
                              transaction_detail=data.get('transaction_detail'),
                              amount_available=data['amount_available'],
                              status=data['status'],
                              forward_balance=data['forward_balance'])
    transaction.save()
    return jsonify(transaction.serialize()), 201

@transaction_bp.route('/transaction/<int:id>', methods=['PUT'])
def update_transaction(id):
    transaction = Transaction.query.get(id)
    if not transaction:
        return jsonify(error="Transaction not found"), 404
    data = request.get_json()
    transaction.date = data.get('date', transaction.date)
    transaction.description = data.get('description', transaction.description)
    transaction.amount = data.get('amount', transaction.amount)
    transaction.currency = data.get('currency', transaction.currency)
    transaction.type_id = data.get('type_id', transaction.type_id)
    transaction.customer_info = data.get('customer_info', transaction.customer_info)
    transaction.bank_info = data.get('bank_info', transaction.bank_info)
    transaction.guess_entry_date = data.get('guess_entry_date', transaction.guess_entry_date)
    transaction.transaction_detail = data.get('transaction_detail', transaction.transaction_detail)
    transaction.amount_available = data.get('amount_available', transaction.amount_available)
    transaction.status = data.get('status', transaction.status)
    transaction.forward_balance = data.get('forward_balance', transaction.forward_balance)
    transaction.save()
    return jsonify(transaction.serialize())

@transaction_bp.route('/transaction/<int:id>', methods=['DELETE'])
def delete_transaction(id):
    transaction = Transaction.query.get(id)
    if not transaction:
        return jsonify(error="Transaction not found"), 404
    transaction.delete()
    return jsonify(message="Transaction deleted")


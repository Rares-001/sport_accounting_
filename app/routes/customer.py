from flask import Blueprint, jsonify, request
from app.models.customer import Customer


customer_bp = Blueprint('customer', __name__, url_prefix='/customer')

@customer_bp.route('/', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    result = []
    for customer in customers:
        result.append({
            'customer_id': customer.customer_id,
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'email': customer.email,
            'phone_number': customer.phone_number,
            'address': customer.address,
            'city': customer.city
        })
    return jsonify(result)

@customer_bp.route('/', methods=['POST'])
def add_customer():
    data = request.json
    customer = Customer(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        phone_number=data['phone_number'],
        address=data['address'],
        city=data['city']
    )
    customer.save()
    return jsonify({
        'message': 'Customer added successfully',
        'customer_id': customer.customer_id
    })

@customer_bp.route('/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = Customer.query.filter_by(customer_id=customer_id).first_or_404()
    result = {
        'customer_id': customer.customer_id,
        'first_name': customer.first_name,
        'last_name': customer.last_name,
        'email': customer.email,
        'phone_number': customer.phone_number,
        'address': customer.address,
        'city': customer.city
    }
    return jsonify(result)

@customer_bp.route('/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    customer = Customer.query.filter_by(customer_id=customer_id).first_or_404()
    data = request.json
    customer.first_name = data.get('first_name', customer.first_name)
    customer.last_name = data.get('last_name', customer.last_name)
    customer.email = data.get('email', customer.email)
    customer.phone_number = data.get('phone_number', customer.phone_number)
    customer.address = data.get('address', customer.address)
    customer.city = data.get('city', customer.city)
    customer.save()
    return jsonify({
        'message': 'Customer updated successfully',
        'customer_id': customer.customer_id
    })

@customer_bp.route('/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    customer = Customer.query.filter_by(customer_id=customer_id).first_or_404()
    customer.delete()
    return jsonify({
        'message': 'Customer deleted successfully',
        'customer_id': customer.customer_id
    })


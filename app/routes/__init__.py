from flask import Blueprint

bp = Blueprint('routes', __name__)

from . import auth, bank, club, customer, transaction, user


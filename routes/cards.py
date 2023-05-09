from flask import Blueprint

from controllers.cards_controller import get_all, get_one

cards = Blueprint('cards', __name__)

cards.route('/getall', methods=["GET"])(get_all)
cards.route('/get/<name>', methods=["GET"])(get_one)
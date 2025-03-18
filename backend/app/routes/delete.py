from flask import Blueprint, jsonify, request, send_from_directory, current_app
from app.models import Food, Drink
from app import db

bp = Blueprint('delete', __name__)

@db.route('/foods/<int:id>', methods=['DELETE'])
def delete_food(id):
    food = Food.query.get_or_404(id)
    db.session.delete(food)
    db.session.commit()
    return jsonify({'message': 'Food deleted successfully!'})


@bp.route('/drinks/<int:id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get_or_404(id)
    db.session.delete(drink)
    db.session.commit()
    return jsonify({'message': 'Drink deleted successfully!'})

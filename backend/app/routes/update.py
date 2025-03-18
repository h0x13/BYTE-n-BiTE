from flask import Blueprint, jsonify, request, send_from_directory, current_app
from app.models import Food, Drink
from app import db

bp = Blueprint('update', __name__)


@bp.route('/foods/<int:id>', methods=['PUT'])
def update_food(id):
    food = Food.query.get_or_404(id)
    data = request.json
    
    if 'price' in data and (not isinstance(data['price'], (int, float)) or data['price'] <= 0):
        return jsonify({'error': 'Price must be a positive number'}), 400
    
    if 'stock' in data and (not isinstance(data['stock'], int) or data['stock'] < 0):
        return jsonify({'error': 'Stock must be a non-negative integer'}), 400
    
    food.name = data.get('name', food.name)
    food.price = data.get('price', food.price)
    food.stock = data.get('stock', food.stock)
    food.image = data.get('image', food.image)
    food.type = data.get('type', food.type)
    
    db.session.commit()
    return jsonify({'message': 'Food updated successfully!'})


@bp.route('/drinks', methods=['POST'])
def add_drink():
    data = request.json
    new_drink = Drink(
        name=data['name'],
        price=data['price'],
        size=data.get('size'),
        stock=data.get('stock', 50),
        image=data.get('image'),
        type=data['type']
    )
    db.session.add(new_drink)
    db.session.commit()
    return jsonify({'message': 'Drink added successfully!'}), 201


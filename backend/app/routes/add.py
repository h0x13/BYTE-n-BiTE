from flask import Blueprint, jsonify, request, send_from_directory, current_app
from app.models import Food, Drink
from app import db

bp = Blueprint('add', __name__)


@bp.route('/foods', methods=['POST'])
def add_food():
    data = request.json
    
    if not data or not all(key in data for key in ['name', 'price', 'type']):
        return jsonify({'error': 'Missing required fields'}), 400
    
    if not isinstance(data['price'], (int, float)) or data['price'] <= 0:
        return jsonify({'error': 'Price must be a positive number'}), 400
    
    if 'stock' in data and (not isinstance(data['stock'], int) or data['stock'] < 0):
        return jsonify({'error': 'Stock must be a non-negative integer'}), 400
    
    new_food = Food(
        name=data['name'],
        price=data['price'],
        stock=data.get('stock', 50),
        image=data.get('image'),
        type=data['type']
    )
    db.session.add(new_food)
    db.session.commit()
    return jsonify({'message': 'Food added successfully!'}), 201

@bp.route('/drinks/<int:id>', methods=['PUT'])
def update_drink(id):
    drink = Drink.query.get_or_404(id)
    data = request.json
    drink.name = data.get('name', drink.name)
    drink.price = data.get('price', drink.price)
    drink.size = data.get('size', drink.size)
    drink.stock = data.get('stock', drink.stock)
    drink.image = data.get('image', drink.image)
    drink.type = data.get('type', drink.type)
    db.session.commit()
    return jsonify({'message': 'Drink updated successfully!'})


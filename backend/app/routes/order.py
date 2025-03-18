from flask import Blueprint, jsonify, request
from app.models import Transaction, Order, Food, Drink
from app import db

bp = Blueprint('transaction', __name__)

@bp.route('/order', methods=['POST'])
def create_order():
    data = request.get_json()
    customer_name = data.get('customer_name')
    payment_method = data.get('payment_method')
    service_type = data.get('service_type')

    items = data.get('items')

    if not customer_name or not items:
        return jsonify({"error": "Customer name and items are required"}), 400

    # Count the quantity of each item
    item_counts = {}
    for item in items:
        item_key = (item['name'], item['price'])  # Use name and price as the key
        if item_key in item_counts:
            item_counts[item_key]['quantity'] += 1
        else:
            item_counts[item_key] = {
                'name': item['name'],
                'price': item['price'],
                'quantity': 1
            }

    # Calculate the total amount
    total_amount = sum(item['price'] * item['quantity'] for item in item_counts.values())

    # Create a new transaction
    transaction = Transaction(
        customer_name=customer_name,
        total_amount=total_amount,
        service_type=service_type,
        payment_method=payment_method,
        status='Pending'
    )
    db.session.add(transaction)
    db.session.commit()

    # Create orders for each item
    for item_key, item_data in item_counts.items():
        name, price = item_key

        # Determine if the item is Food or Drink
        food_item = Food.query.filter_by(name=name, price=price).first()
        drink_item = Drink.query.filter_by(name=name, price=price).first()

        if food_item:
            item_type = 'Food'
            item_id = food_item.id  # Use the ID from the Food table
        elif drink_item:
            item_type = 'Drink'
            item_id = drink_item.id  # Use the ID from the Drink table
        else:
            # If the item is neither Food nor Drink, skip it or handle the error
            continue

        order = Order(
            item_id=item_id,  # Use the ID from the corresponding table
            item_type=item_type,  # Set the correct item type
            quantity=item_data['quantity'],
            price=item_data['price'],
            transaction_id=transaction.id
        )
        db.session.add(order)

    db.session.commit()

    return jsonify({"message": "Order created successfully", "transaction_id": transaction.id}), 201

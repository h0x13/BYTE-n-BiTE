from flask import Blueprint, jsonify
from app.models import Order

bp = Blueprint('get_orders', __name__)


@bp.route('/transaction/<int:transaction_id>/orders', methods=['GET'])
def get_orders_by_transaction(transaction_id):
    # Fetch all orders associated with the transaction
    orders = Order.query.filter_by(transaction_id=transaction_id).all()
    if not orders:
        return jsonify({"error": "No orders found for this transaction"}), 404

    # Convert orders to a list of dictionaries
    orders_data = []
    for order in orders:
        order_data = {
            "id": order.id,
            "item_id": order.item_id,
            "item_type": order.item_type,
            "quantity": order.quantity,
            "price": order.price,
            "transaction_id": order.transaction_id,
            "created_at": order.created_at.isoformat(),
            "updated_at": order.updated_at.isoformat()
        }
        orders_data.append(order_data)

    return jsonify(orders_data)

@bp.route('/order/<int:order_id>', methods=['GET'])
def get_order_by_id(order_id):
    # Fetch the order by ID
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    # Convert the order to a dictionary
    order_data = {
        "id": order.id,
        "item_id": order.item_id,
        "item_type": order.item_type,
        "quantity": order.quantity,
        "price": order.price,
        "transaction_id": order.transaction_id,
        "created_at": order.created_at.isoformat(),
        "updated_at": order.updated_at.isoformat()
    }

    return jsonify(order_data)

@bp.route('/orders', methods=['GET'])
def get_all_orders():
    # Fetch all orders
    orders = Order.query.all()
    if not orders:
        return jsonify({"error": "No orders found"}), 404

    # Convert orders to a list of dictionaries
    orders_data = []
    for order in orders:
        order_data = {
            "id": order.id,
            "item_id": order.item_id,
            "item_type": order.item_type,
            "quantity": order.quantity,
            "price": order.price,
            "transaction_id": order.transaction_id,
            "created_at": order.created_at.isoformat(),
            "updated_at": order.updated_at.isoformat()
        }
        orders_data.append(order_data)

    return jsonify(orders_data)

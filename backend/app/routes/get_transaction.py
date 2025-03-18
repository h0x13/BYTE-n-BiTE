from app.models import Transaction
from flask import Blueprint, jsonify

bp = Blueprint('get_transaction', __name__)


@bp.route('/transactions', methods=['GET'])
def get_all_transactions():
    # Fetch all transactions
    transactions = Transaction.query.all()
    if not transactions:
        return jsonify({"error": "No transactions found"}), 404

    # Convert transactions to a list of dictionaries
    transactions_data = []
    for transaction in transactions:
        transaction_data = {
            "id": transaction.id,
            "customer_name": transaction.customer_name,
            "total_amount": transaction.total_amount,
            "status": transaction.status,
            "created_at": transaction.created_at.isoformat(),
            "updated_at": transaction.updated_at.isoformat()
        }
        transactions_data.append(transaction_data)

    return jsonify(transactions_data)

@bp.route('/transaction/<int:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    # Fetch the transaction by ID
    transaction = Transaction.query.get(transaction_id)
    if not transaction:
        return jsonify({"error": "Transaction not found"}), 404

    # Convert the transaction to a dictionary
    transaction_data = {
        "id": transaction.id,
        "customer_name": transaction.customer_name,
        "total_amount": transaction.total_amount,
        "status": transaction.status,
        "created_at": transaction.created_at.isoformat(),
        "updated_at": transaction.updated_at.isoformat()
    }

    return jsonify(transaction_data)



from . import db
from datetime import datetime

class Food(db.Model):
    __tablename__ = 'foods'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=50)
    image = db.Column(db.String, nullable=True)
    type = db.Column(db.String, nullable=False)  # e.g., 'Bread', 'Filling', 'Spread'

    def __repr__(self):
        return f"<Food(name={self.name}, price={self.price}, type={self.type})>"

class Drink(db.Model):
    __tablename__ = 'drinks'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    size = db.Column(db.String, nullable=True)  # e.g., 'Small', 'Medium', 'Large'
    stock = db.Column(db.Integer, nullable=False, default=50)
    image = db.Column(db.String, nullable=True)
    type = db.Column(db.String, nullable=False)  # e.g., 'Flavor', 'Add-on'

    def __repr__(self):
        return f"<Drink(name={self.name}, price={self.price}, size={self.size}, type={self.type})>"

class Transaction(db.Model):
    __tablename__ = 'transactions'
    
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    service_type = db.Column(db.String, nullable=False, default='pickup')
    payment_method = db.Column(db.String, nullable=False, default='cash')
    status = db.Column(db.String, nullable=False)  # e.g., 'Completed', 'Pending', 'Cancelled'
    
    orders = db.relationship('Order', back_populates='transaction')
    
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    def __repr__(self):
        return f"<Transaction(id={self.id}, customer_name={self.customer_name}, total_amount={self.total_amount}, status={self.status})>"

class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, nullable=False)  # Can be food_id or drink_id
    item_type = db.Column(db.String, nullable=False)  # 'Food' or 'Drink'
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)  # Price at the time of the order
    
    transaction_id = db.Column(db.Integer, db.ForeignKey('transactions.id'), nullable=False)
    
    transaction = db.relationship('Transaction', back_populates='orders')

    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    
    def __repr__(self):
        return f"<Order(id={self.id}, item_id={self.item_id}, item_type={self.item_type}, quantity={self.quantity}, price={self.price})>"

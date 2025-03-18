from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:8080"}})
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import fetch
    from app.routes import order
    from app.routes import get_transaction 
    from app.routes import get_orders

    app.register_blueprint(fetch.bp)
    app.register_blueprint(order.bp)
    app.register_blueprint(get_transaction.bp)
    app.register_blueprint(get_orders.bp)

    return app

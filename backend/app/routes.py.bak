from flask import Blueprint, jsonify, request, send_from_directory, current_app
from app.models import Food, Drink

bp = Blueprint('main', __name__)

def query_to_json(items):
    print(current_app.config['UPLOAD_FOLDER'])
    results = []
    for item in items:
        data = {}
        for key, value in item.__dict__.items():
            if not key.startswith('_'):
                if key == 'image':
                    data[key] = f"{request.host}/image/{value}"
                else:
                    data[key] = value
        results.append(data)
    return results

@bp.route('/foods')
def get_foods():
    return jsonify(query_to_json(Food.query.all()))

@bp.route('/drinks')
def get_drinks():
    return jsonify(query_to_json(Drink.query.all()))

@bp.route('/foods/<string:type>')
def get_foods_by_type(type):
    return jsonify(query_to_json(Food.query.filter_by(type=type)))

@bp.route('/drinks/<string:type>')
def get_drinks_by_type(type):
    return jsonify(query_to_json(Drink.query.filter_by(type=type)))

@bp.route('/image/<filename>')
def get_file(filename):
    try:
        return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)
    except Exception as e:
        current_app.logger.error(f"Error serving file {filename}: {str(e)}")
        return jsonify({"error": "File not found or permission denied"}), 404

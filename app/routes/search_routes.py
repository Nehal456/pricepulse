from flask import Blueprint, request, jsonify

search_bp = Blueprint('search', __name__)

@search_bp.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('q')
    brand = request.args.get('brand')
    price_range = request.args.get('price_range')

    # Just for test — normally you'd call external APIs or your DB
    sample_products = [
        {"name": "Samsung Galaxy A13", "brand": "samsung", "price": 11999},
        {"name": "Samsung M14", "brand": "samsung", "price": 14999},
    ]

    filtered = []
    if price_range:
        min_price, max_price = map(int, price_range.split('-'))
        for product in sample_products:
            if (not brand or product["brand"].lower() == brand.lower()) and \
               (min_price <= product["price"] <= max_price):
                filtered.append(product)

    return jsonify(filtered)

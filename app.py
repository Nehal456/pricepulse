from flask import Flask, request, jsonify
import json

app = Flask(__name__)

with open('products.json') as f:
    products = json.load(f)

@app.route('/search')
def search_products():
    query = request.args.get('q', '').lower()
    min_price = float(request.args.get('min_price', 0))
    max_price = float(request.args.get('max_price', float('inf')))
    sort_by = request.args.get('sort_by', '')  # price, name, rating
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))

    filtered = [
        product for product in products
        if query in product['name'].lower() or query in product['brand'].lower() or query in product['category'].lower()
    ]

    filtered = [p for p in filtered if min_price <= p['price'] <= max_price]

    if sort_by == 'price':
        filtered.sort(key=lambda x: x['price'])
    elif sort_by == 'name':
        filtered.sort(key=lambda x: x['name'])
    elif sort_by == 'rating':
        filtered.sort(key=lambda x: x.get('rating', 0), reverse=True)

    start = (page - 1) * limit
    end = start + limit
    paginated = filtered[start:end]

    return jsonify({
        "total_results": len(filtered),
        "page": page,
        "limit": limit,
        "results": paginated
    })

if __name__ == '__main__':
    app.run(debug=True)

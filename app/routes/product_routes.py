from flask import Blueprint, render_template, request
from app.utils.scraper import get_top_amazon_results

product_bp = Blueprint('product', __name__)

@product_bp.route('/')
def home():
    return render_template('home.html')

@product_bp.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        results = get_top_amazon_results(query)
        return render_template('results.html', results=results)
    return render_template('search.html')

@product_bp.route('/add-from-search', methods=['POST'])
def add_from_search():
    # Save selected product to CSV
    # (Same as described earlier)
    ...
import csv

@product_bp.route('/')
def home():
    products = []
    try:
        with open('products.csv', newline='') as f:
            reader = csv.reader(f)
            products = list(reader)
    except FileNotFoundError:
        pass

    return render_template('home.html', products=products)

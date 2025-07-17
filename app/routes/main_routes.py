from flask import Blueprint, render_template, request
from app.scraper.amazon_scraper import get_amazon_results
from app.scraper.flipkart_scraper import get_flipkart_results

# ✅ Define the blueprint
main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@main_bp.route("/search", methods=["POST"])
def search():
    query = request.form.get("query")
    amazon_results = get_amazon_results(query)
    flipkart_results = get_flipkart_results(query)
    return render_template("results.html", query=query, amazon_results=amazon_results, flipkart_results=flipkart_results)

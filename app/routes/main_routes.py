from flask import Blueprint, render_template, request
from app.scraper.amazon_scraper import get_amazon_results
from app.scraper.flipkart_scraper import get_flipkart_results

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["GET", "POST"])
def home():
    amazon_results = []
    flipkart_results = []

    if request.method == "POST":
        query = request.form["query"]
        amazon_results = get_amazon_results(query)
        flipkart_results = get_flipkart_results(query)

    return render_template("home.html", amazon_results=amazon_results, flipkart_results=flipkart_results)

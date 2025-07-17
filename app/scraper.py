import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def scrape_amazon(product_name):
    query = quote_plus(product_name)
    url = f"https://www.amazon.in/s?k={query}"

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    results = []
    for item in soup.select('.s-result-item'):
        title_tag = item.select_one('h2 span')
        price_tag = item.select_one('.a-price .a-offscreen')
        link_tag = item.select_one('h2 a')

        if title_tag and price_tag and link_tag:
            title = title_tag.text.strip()
            price = price_tag.text.strip()
            link = "https://www.amazon.in" + link_tag['href']
            results.append({"title": title, "price": price, "link": link})

        if len(results) >= 5:
            break

    return results

def scrape_flipkart(product_name):
    query = quote_plus(product_name)
    url = f"https://www.flipkart.com/search?q={query}"

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    results = []
    for item in soup.select('._1AtVbE'):
        title_tag = item.select_one('div._4rR01T')
        price_tag = item.select_one('div._30jeq3')
        link_tag = item.select_one('a._1fQZEK')

        if title_tag and price_tag and link_tag:
            title = title_tag.text.strip()
            price = price_tag.text.strip()
            link = "https://www.flipkart.com" + link_tag['href']
            results.append({"title": title, "price": price, "link": link})

        if len(results) >= 5:
            break

    return results

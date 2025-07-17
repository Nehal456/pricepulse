import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def scrape_prices():
    url = "https://www.amazon.in/s?k=keyboard"  # or dynamic URL
    headers = {
        "User-Agent": UserAgent().random,
    }

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        results = []

        for item in soup.select(".s-result-item[data-asin]")[:5]:  # limit results
            title = item.select_one("h2 span")
            price = item.select_one(".a-price .a-offscreen")
            link = item.select_one("h2 a")

            if title and price and link:
                results.append({
                    "title": title.text.strip(),
                    "price": price.text.strip(),
                    "link": f"https://www.amazon.in{link['href']}"
                })

        return results or [{"title": "No items found", "price": "-", "link": "#"}]

    except Exception as e:
        return [{"title": f"Error: {str(e)}", "price": "-", "link": "#"}]

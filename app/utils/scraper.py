import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

def get_top_amazon_results(query, max_results=5):
    search_query = f"{query} site:amazon.in"
    url = f"https://www.google.com/search?q={quote_plus(search_query)}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    results = []
    for g in soup.find_all('div', class_='g'):
        link = g.find('a', href=True)
        title = g.find('h3')
        if link and title and "amazon.in" in link['href']:
            results.append({
                "title": title.text,
                "url": link['href']
            })
        if len(results) >= max_results:
            break

    return results

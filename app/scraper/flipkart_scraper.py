def search_flipkart(query, brand='', min_price='', max_price=''):
    headers = {
        "User-Agent": "Mozilla/5.0",
    }

    url = f"https://www.flipkart.com/search?q={query.replace(' ', '+')}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    items = []
    for product in soup.select("._1AtVbE"):
        title = product.select_one("._4rR01T")
        price = product.select_one("._30jeq3")
        link = product.select_one("a")
        image = product.select_one("img")

        if not title or not price or not link:
            continue

        title_text = title.text.strip()
        price_value = int(price.text.replace("₹", "").replace(",", "").strip())
        product_link = "https://www.flipkart.com" + link.get("href")
        image_url = image["src"] if image else ""

        # 🔍 Apply filters
        if brand and brand.lower() not in title_text.lower():
            continue
        if min_price and price_value < int(min_price):
            continue
        if max_price and price_value > int(max_price):
            continue

        items.append({
            "title": title_text,
            "price": price_value,
            "link": product_link,
            "image": image_url,
            "source": "Flipkart"
        })

    return items

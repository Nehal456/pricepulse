def search_amazon(query, brand='', min_price='', max_price=''):
    headers = {
        "User-Agent": "Mozilla/5.0",
    }

    url = f"https://www.amazon.in/s?k={query.replace(' ', '+')}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    items = []
    for product in soup.select(".s-result-item"):
        title = product.select_one("h2 span")
        price = product.select_one(".a-price-whole")
        link = product.select_one("h2 a")
        image = product.select_one(".s-image")

        if not title or not price or not link:
            continue

        title_text = title.text.strip()
        price_value = int(price.text.replace(",", "").strip())
        product_link = "https://www.amazon.in" + link.get("href")
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
            "source": "Amazon"
        })

    return items

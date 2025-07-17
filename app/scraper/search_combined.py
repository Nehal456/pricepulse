def search_all_sites(query, brand='', min_price='', max_price='', site=''):
    results = []

    if site in ('', 'amazon'):
        results += search_amazon(query, brand, min_price, max_price)

    if site in ('', 'flipkart'):
        results += search_flipkart(query, brand, min_price, max_price)

    return results

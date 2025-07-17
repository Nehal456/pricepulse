import json
import random

categories = {
    "electronics": ["Smartphone", "Laptop", "Tablet", "Smartwatch", "Bluetooth Speaker", "Earbuds"],
    "garments": ["T-Shirt", "Jeans", "Jacket", "Kurti", "Sweater", "Socks"],
    "fitness": ["Yoga Mat", "Dumbbells", "Treadmill", "Skipping Rope", "Fitness Tracker"],
    "groceries": ["Rice 5kg", "Wheat Flour", "Milk 1L", "Eggs 12pcs", "Almonds 500g", "Honey"],
    "kitchen": ["Pressure Cooker", "Frying Pan", "Microwave Oven", "Toaster", "Knife Set"],
    "beauty": ["Face Wash", "Shampoo", "Lipstick", "Moisturizer", "Sunscreen"],
    "baby": ["Baby Diapers", "Baby Shampoo", "Feeding Bottle", "Baby Wipes"],
    "toys": ["Teddy Bear", "Remote Car", "Lego Set", "Puzzle", "Action Figure"],
    "automobile": ["Car Vacuum", "Seat Cover", "Phone Holder", "Tyre Inflator"],
    "stationery": ["Notebook", "Pen Set", "Highlighters", "Sticky Notes", "Stapler"]
}

brands = {
    "electronics": ["Samsung", "Apple", "OnePlus", "Xiaomi", "Sony"],
    "garments": ["Zara", "H&M", "Levi's", "Puma", "Nike"],
    "fitness": ["Decathlon", "HRX", "Fitkit", "Boldfit"],
    "groceries": ["BigBasket", "AmazonFresh", "Grofers"],
    "kitchen": ["Prestige", "Pigeon", "Butterfly", "Borosil"],
    "beauty": ["Nivea", "Lakme", "Mamaearth", "Dove"],
    "baby": ["Pampers", "Huggies", "Johnson's"],
    "toys": ["ToyZone", "HotWheels", "Lego", "Funskool"],
    "automobile": ["Steelbird", "Autofy", "Michelin"],
    "stationery": ["Classmate", "Camlin", "Faber-Castell"]
}

product_list = []
product_id = 1

for category, items in categories.items():
    for _ in range(10):  # generate 10 products per category
        name = random.choice(items)
        brand = random.choice(brands[category])
        price = random.randint(100, 100000) if category == "electronics" else random.randint(50, 10000)

        product = {
            "id": product_id,
            "name": f"{brand} {name}",
            "brand": brand,
            "category": category,
            "price": price
        }

        product_list.append(product)
        product_id += 1

# Save to JSON
with open("products.json", "w") as file:
    json.dump(product_list, file, indent=4)

print(f"✅ Successfully generated {len(product_list)} products in products.json")

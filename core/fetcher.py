import csv
import os
from config.settings import DATA_DIR

INPUT_FILE = os.path.join(DATA_DIR, "products.csv")
OUTPUT_FILE = os.path.join(DATA_DIR, "product_data.csv")

def crawl_all():
    product_data = []

    with open(INPUT_FILE, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            product_data.append({
                "name": row["name"],
                "url": row["url"],
                "price": 19.99  # Simulated price
            })

    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "url", "price"])
        writer.writeheader()
        writer.writerows(product_data)
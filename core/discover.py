import csv
import os
from config.settings import DATA_DIR

OUTPUT_FILE = os.path.join(DATA_DIR, "products.csv")

def main():
    products = [
        {"name": "Widget A", "url": "https://example.com/widget-a"},
        {"name": "Widget B", "url": "https://example.com/widget-b"},
    ]

    os.makedirs(DATA_DIR, exist_ok=True)

    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "url"])
        writer.writeheader()
        writer.writerows(products)
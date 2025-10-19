# Product Price Intel Crawler & Tracker

This project is a two-phase system for extracting and monitoring product prices from a predefined list of product URLs. It supports initial data collection and ongoing change tracking.

- Uses a static list of product URLs in products.csv for the initial crawl.
- The crawler reads this list, extracts product data, and saves it to product_data.csv.
- The tracker then uses product_data.csv to monitor changes over time.

## Setup

1. Install dependencies:

   ```bash
   pip install requests beautifulsoup4
Prepare your input file: ```

Create data/products.csv with the following format:

 ```csv
name,url

AirPods Pro,https://www.apple.com/shop/product/MLWK3AM/A/airpods-pro
Sony WH-1000XM5,https://www.sony.com/electronics/headband-headphones/wh-1000xm5```

## Configure settings:
Edit config/settings.py to define paths and crawler behavior:

 ```import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
USER_AGENT = "Mozilla/5.0 ..."
TIMEOUT = 10

os.makedirs(DATA_DIR, exist_ok=True) ```

## Phase 1: Initial Crawl
Run the crawler to extract product titles and prices from your predefined list:
python3 core/crawl.py
- Reads from products.csv
- Visits each product URL
- Extracts product title and price
- Saves results to product_data.csv

## Phase 2: Tracker
Run the tracker to detect updates in product data:
python3 core/track.py
- Reads from product_data.csv
- Re-fetches each product page
- Compares current vs previous price
- Saves changes to product_changes.csv

##  Notes
- This crawler uses a predefined list of product URLs. It does not auto-discover product pages.
- Price extraction relies on simple HTML selectors (span.price, etc). You may need to customize these per domain.
- For dynamic sites (e.g. JavaScript-rendered prices), consider integrating a headless browser like Selenium or Playwright.


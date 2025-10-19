Product Price Crawler & Tracker
This project is a two-phase system for extracting and monitoring product prices from a predefined list of product URLs. It supports initial data collection and ongoing change tracking.

Project Structure
Code
project-root/
├── config/
│   └── settings.py         # Global settings and paths
├── core/
│   ├── crawl.py            # Phase 1: Extract product data from predefined URLs
│   └── track.py            # Phase 2: Monitor changes in product data
├── data/
│   ├── products.csv        # Input: list of product URLs (name,url)
│   ├── product_data.csv    # Output: full product data from crawl
│   └── product_changes.csv # Output: tracked changes from tracker
└── README.md               # Project documentation
Setup
Install dependencies:

Code
pip install requests beautifulsoup4
Prepare your input file: Create data/products.csv with the following format:

Code
name,url
AirPods Pro,https://www.apple.com/shop/product/MLWK3AM/A/airpods-pro
Sony WH-1000XM5,https://www.sony.com/electronics/headband-headphones/wh-1000xm5
Configure settings: Edit config/settings.py to define paths and crawler behavior:

python
BASE_DIR = ...
DATA_DIR = ...
USER_AGENT = ...
TIMEOUT = ...
Phase 1: Initial Crawl
Run the crawler to extract product titles and prices from your predefined list:

Code
python3 core/crawl.py
Reads from products.csv

Visits each product URL

Extracts product title and price

Saves results to product_data.csv

Phase 2: Tracker
Run the tracker to detect updates in product data:

Code
python3 core/track.py
Reads from product_data.csv

Re-fetches each product page

Compares current vs previous price

Saves changes to product_changes.csv

Notes
This crawler uses a predefined list of product URLs. It does not auto-discover product pages.

Price extraction relies on simple HTML selectors (span.price, etc). You may need to customize these per domain.

For dynamic sites (e.g. JavaScript-rendered prices), consider integrating a headless browser like Selenium or Playwright.

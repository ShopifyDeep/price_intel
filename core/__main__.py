# crawler/main.py

import asyncio
import os
from crawler.discover import main as discover_main
from crawler.fetcher import crawl_all
from crawler.tracker import track_and_update

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
PRODUCTS_FILE = os.path.join(DATA_DIR, "products.csv")
PREVIOUS_FILE = os.path.join(DATA_DIR, "products_previous.csv")
CHANGES_FILE = os.path.join(DATA_DIR, "price_changes.csv")

async def run_discovery():
    print("\n[STEP 1] Discovering product URLs...")
    await discover_main()

async def run_fetcher():
    print("\n[STEP 2] Fetching product data...")
    await crawl_all()

def run_tracker():
    print("\n[STEP 3] Tracking price changes...")
    changes = track_and_update(PRODUCTS_FILE, PREVIOUS_FILE, CHANGES_FILE)
    print(f"[✓] Tracker complete — {len(changes)} changes detected")

async def main():
    await run_discovery()
    await run_fetcher()
    run_tracker()

if __name__ == "__main__":
    asyncio.run(main())
import argparse
import os
from core.discover import main as discover_main
from core.fetcher import crawl_all
from core.tracker import track_and_update
from core.logger import logger
from config.settings import DATA_DIR

def run_pipeline():
    logger.info("STEP 1: Discovering product URLs...")
    discover_main()

    logger.info("STEP 2: Fetching product data...")
    crawl_all()

    logger.info("STEP 3: Tracking price changes...")
    current_file = os.path.join(DATA_DIR, "product_data.csv")
    previous_file = os.path.join(DATA_DIR, "product_data_previous.csv")
    changes_file = os.path.join(DATA_DIR, "price_changes.csv")
    track_and_update(current_file, previous_file, changes_file)

    logger.info("✓ Pipeline complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the price intelligence crawler.")
    parser.add_argument("--run", action="store_true", help="Run the full pipeline")
    args = parser.parse_args()

    if args.run:
        run_pipeline()

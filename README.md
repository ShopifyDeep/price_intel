# Product Price Crawler & Tracker

This project is a two-phase system for extracting and monitoring product prices from a predefined list of product URLs. It supports initial data collection and ongoing change tracking.

## Project Structure

project-root/ ├── config/ │ └── settings.py # Global settings and paths ├── core/ │ ├── crawl.py # Phase 1: Extract product data from predefined URLs │ └── track.py # Phase 2: Monitor changes in product data ├── data/ │ ├── products.csv # Input: list of product URLs (name,url) │ ├── product_data.csv # Output: full product data from crawl │ └── product_changes.csv # Output: tracked changes from tracker └── README.md # Project documentation

## Setup

1. Install dependencies:

   ```bash
   pip install requests beautifulsoup4
Prepare your input file:

Create data/products.csv with the following format:

csv
name,url
AirPods Pro,https://www.apple.com/shop/product/MLWK3AM/A/airpods-pro
Sony WH-1000XM5,https://www.sony.com/electronics/headband-headphones/wh-1000xm5
Configure settings:


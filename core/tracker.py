# crawler/tracker.py

import os
import csv
from datetime import datetime

def load_previous_data(filepath):
    """Load historical product data from CSV into a dict keyed by product_url."""
    previous = {}
    try:
        with open(filepath, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                previous[row['product_url']] = row
    except FileNotFoundError:
        print(f"[!] No previous data found at {filepath}")
    return previous

def compute_price_delta(old_price, new_price):
    """Compute price difference and percentage change."""
    try:
        old = float(old_price.replace('$', '').replace(',', ''))
        new = float(new_price.replace('$', '').replace(',', ''))
        delta = new - old
        percent = (delta / old) * 100 if old else 0
        return f"{delta:.2f} ({percent:+.1f}%)"
    except:
        return ""

def detect_changes(previous, current):
    """Compare current crawl with previous data and return changed items."""
    changes = []

    for item in current:
        url = item['product_url']
        old = previous.get(url)

        if not old:
            item['change_type'] = 'new'
            changes.append(item)
            continue

        changed_fields = []
        for field in ['price', 'currency', 'sku', 'product_title']:
            if item.get(field) != old.get(field):
                changed_fields.append(field)

        if changed_fields:
            item['change_type'] = 'updated'
            item['changed_fields'] = ','.join(changed_fields)
            item['previous_price'] = old.get('price', '')
            item['price_delta'] = compute_price_delta(old.get('price'), item.get('price'))
            item['change_timestamp'] = datetime.utcnow().isoformat()
            changes.append(item)

    return changes

def track_and_update(current_file, previous_file, changes_file):
    """Compare current crawl to previous. If no previous, save baseline."""
    if not os.path.exists(previous_file):
        print("[!] No previous crawl found — saving baseline")
        os.rename(current_file, previous_file)
        return []

    previous = load_previous_data(previous_file)
    with open(current_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        current = list(reader)

    changes = detect_changes(previous, current)

    if changes:
        with open(changes_file, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=changes[0].keys())
            writer.writeheader()
            writer.writerows(changes)
        print(f"[✓] Saved {len(changes)} changes to {changes_file}")
    else:
        print("[✓] No changes detected")

    os.replace(current_file, previous_file)
    return changes
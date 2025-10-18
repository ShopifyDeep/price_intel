import os

# === File Paths ===
DATA_DIR = os.path.join(os.getcwd(), "data")
LOG_DIR = os.path.join(os.getcwd(), "logs")

# === URLs ===
BASE_URL = "https://example.com/products"

# === Thresholds ===
PRICE_DROP_THRESHOLD = 0.05  # 5% drop

# === Environment Flags ===
DEBUG_MODE = os.getenv("DEBUG_MODE", "false").lower() == "true"
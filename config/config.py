"""
config.py — Centralized configuration loader.
Reads from secrets.env and provides typed settings throughout the app.
All city/location settings are driven by env vars — no hardcoded city names.
"""

import os
from dotenv import load_dotenv

load_dotenv("secrets.env")

# ── Telegram ──────────────────────────────────────────────────────────────────
TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID: str   = os.getenv("TELEGRAM_CHAT_ID", "")

# ── User Location ─────────────────────────────────────────────────────────────
USER_LOCALITY: str  = os.getenv("USER_LOCALITY", "My Area")
USER_LAT: float     = float(os.getenv("USER_LAT", "0.0"))
USER_LON: float     = float(os.getenv("USER_LON", "0.0"))
SEARCH_RADIUS_KM: float = float(os.getenv("SEARCH_RADIUS_KM", "7"))

# City settings — used to build Zomato URLs and filter area names
# USER_CITY      : Display name shown in Telegram messages  (e.g. "Kolkata")
# USER_CITY_SLUG : Lowercase URL slug on zomato.com          (e.g. "kolkata")
# ZOMATO_CITY_ID : Zomato's internal numeric city ID         (e.g. 4 for Kolkata)
#                  Find yours: open zomato.com/YOUR_CITY, check network requests
USER_CITY: str      = os.getenv("USER_CITY", "My City")
USER_CITY_SLUG: str = os.getenv("USER_CITY_SLUG", "").lower().strip()
ZOMATO_CITY_ID: int = int(os.getenv("ZOMATO_CITY_ID", "0"))

# ── Scheduler ─────────────────────────────────────────────────────────────────
NOTIFY_HOUR: int   = int(os.getenv("NOTIFY_HOUR", "18"))
NOTIFY_MINUTE: int = int(os.getenv("NOTIFY_MINUTE", "0"))

# ── Scraper ───────────────────────────────────────────────────────────────────
TOP_DEALS_COUNT: int         = int(os.getenv("TOP_DEALS_COUNT", "10"))
MIN_DISCOUNT_PERCENT: int    = int(os.getenv("MIN_DISCOUNT_PERCENT", "10"))
REQUEST_DELAY_SECONDS: float = float(os.getenv("REQUEST_DELAY_SECONDS", "2"))

# ── Paths ─────────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH  = os.path.join(BASE_DIR, "db", "deals.db")
LOG_PATH = os.path.join(BASE_DIR, "logs", "app.log")

# ── Zomato auth cookies (from browser DevTools) ───────────────────────────────
ZOMATO_COOKIES: str = os.getenv("ZOMATO_COOKIES", "")

# ── Swiggy uses the same lat/lon as user location ─────────────────────────────
SWIGGY_LAT = USER_LAT
SWIGGY_LON = USER_LON


def validate():
    """Call at startup to catch missing critical config."""
    missing = []
    if not TELEGRAM_BOT_TOKEN:
        missing.append("TELEGRAM_BOT_TOKEN")
    if not TELEGRAM_CHAT_ID:
        missing.append("TELEGRAM_CHAT_ID")
    if USER_LAT == 0.0 or USER_LON == 0.0:
        missing.append("USER_LAT / USER_LON  (must be non-zero coordinates)")
    if not USER_CITY_SLUG:
        missing.append("USER_CITY_SLUG  (e.g. 'kolkata', 'mumbai', 'bangalore')")
    if missing:
        raise EnvironmentError(
            f"Missing / invalid env vars: {', '.join(missing)}\n"
            f"Please fill in your secrets.env file."
        )

# 🍽️ DealBot — Restaurant Deal Tracker (Any City)

Automatically scrapes **Zomato and Swiggy** for the best restaurant deals **in any city**, ranks them by discount %, stores them daily, and sends a **Telegram notification at your specified time through the day!**.

---

## 🌍 Now Supports Any City

You can configure it for **any city** by updating:

```env
USER_CITY=Kolkata
USER_CITY_SLUG=kolkata
```

### 🧠 What these mean:

* `USER_CITY` → Display name (used in messages/logs)
* `USER_CITY_SLUG` → Used in URLs (must match platform format)

---

### 📍 Examples

| City      | USER_CITY | USER_CITY_SLUG |
| --------- | --------- | -------------- |
| Kolkata   | Kolkata   | kolkata        |
| Bangalore | Bangalore | bangalore      |
| Delhi     | Delhi     | ncr            |
| Mumbai    | Mumbai    | mumbai         |
| Hyderabad | Hyderabad | hyderabad      |

---

## 📁 Project Structure

```
dealbot/
├── .env
├── requirements.txt
├── pipeline.py           ← Main orchestration (scrape → rank → store → notify)
├── scheduler.py          ← APScheduler daemon
├── cli.py                ← Command-line tool
│
├── config/
│   └── config.py         ← Loads settings from .env
│
├── scraper/
│   ├── base_scraper.py
│   ├── swiggy_scraper.py
│   ├── zomato_scraper.py
│   └── ranker.py         ← Scoring + deduplication
│
├── db/
│   ├── database.py
│   └── deals.db
│
├── notifier/
│   └── telegram_notifier.py
│
└── logs/
    └── app.log
```

---

## ⚡ Quick Start (5 minutes)

### Step 1 — Install dependencies

```bash
pip install -r requirements.txt
```

---

### Step 2 — Create Telegram Bot

1. Open Telegram
2. Search **@BotFather** → `/newbot`
3. Copy API token

---

### Step 3 — Get Chat ID

1. Search **@userinfobot**
2. Send `/start`
3. Copy your Chat ID

---

### Step 4 — Configure `.env`

```bash
cp .env.example .env
```

Edit:

```env
TELEGRAM_BOT_TOKEN=your_token
TELEGRAM_CHAT_ID=your_chat_id

USER_CITY=Kolkata
USER_CITY_SLUG=kolkata
USER_LAT=22.5804
USER_LON=88.4183
```

---

### Step 5 — Test bot

```bash
python cli.py test-bot
```

---

### Step 6 — Run manually

```bash
python cli.py run
```

---

### Step 7 — Start scheduler

```bash
python scheduler.py
```

---

## 🛠️ CLI Commands

| Command                  | Description    |
| ------------------------ | -------------- |
| `python cli.py run`      | Full pipeline  |
| `python cli.py scrape`   | Scrape only    |
| `python cli.py notify`   | Send deals     |
| `python cli.py top`      | Show top deals |
| `python cli.py stats`    | DB stats       |
| `python cli.py test-bot` | Test Telegram  |
| `python cli.py setup`    | Setup wizard   |

---

## ⚙️ Configuration Options

| Variable                | Description             |
| ----------------------- | ----------------------- |
| `USER_CITY`             | Display city name       |
| `USER_CITY_SLUG`        | Used in URLs            |
| `USER_LAT` / `USER_LON` | Required for Swiggy API |
| `NOTIFY_HOUR`           | Daily notification hour |
| `TOP_DEALS_COUNT`       | Number of deals sent    |

---

## 🧠 How It Works

```
Scraper → Ranker → Database → Telegram Notifier
```

* Scrapes deals from multiple platforms
* Normalizes + deduplicates data
* Ranks based on discount & relevance
* Stores historical data
* Sends daily alerts

---

## 📊 Database

SQLite (`db/deals.db`) stores:

* restaurant_name
* platform (zomato/swiggy)
* discount_pct
* offer_title
* rating
* location
* timestamp

---

## ⚠️ Notes

* APIs may change → fallback parsing is used
* Cookies/session may be required for some endpoints
* Intended for personal use

---

## 🚀 Future Improvements

* Multi-city tracking in one run
* Web dashboard
* ML-based deal prediction
* Cloud deployment (24/7 bot)

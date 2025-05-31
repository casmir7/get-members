# Telegram Group Member Scraper

A simple Python script that uses [Telethon](https://docs.telethon.dev/) to scrape usernames of members from a public Telegram group.

---

## Features

- Scrapes all members from a specified Telegram group
- Outputs the usernames of all members found
- Uses a single Telegram session file for authentication
- Async and efficient with Telethon

---

## Requirements

- Python 3.7+
- Telethon (`pip install telethon`)
- Telegram API credentials (`api_id` and `api_hash`)

---

## Setup

1. **Create a Telegram application** to get your `api_id` and `api_hash`:  
   https://my.telegram.org/apps

2. **Set your credentials as environment variables** (recommended):

   ```bash
   export TELEGRAM_API_ID=your_api_id
   export TELEGRAM_API_HASH=your_api_hash

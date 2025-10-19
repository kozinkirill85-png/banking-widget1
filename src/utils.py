# src/utils.py
from pathlib import Path
import json
import logging
from datetime import datetime
import requests

logger = logging.getLogger(__name__)

def get_greeting(date_str: str) -> str:
    hour = int(date_str.split()[1].split(":")[0])
    if 5 <= hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 18:
        return "Добрый день"
    elif 18 <= hour < 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"

def get_currency_rates(currencies: list) -> list:
    rates = []
    for cur in currencies:
        try:
            res = requests.get(f"https://api.exchangerate-api.com/v4/latest/RUB")
            data = res.json()
            rate = 1 / data["rates"].get(cur, 1)
            rates.append({"currency": cur, "rate": round(rate, 2)})
        except Exception as e:
            logger.error(f"Ошибка получения курса {cur}: {e}")
            rates.append({"currency": cur, "rate": 0})
    return rates

def get_stock_prices(stocks: list) -> list:
    prices = []
    for stock in stocks:
        try:
            # Используем заглушку
            prices.append({"stock": stock, "price": 100.0})
        except Exception as e:
            logger.error(f"Ошибка получения цены {stock}: {e}")
            prices.append({"stock": stock, "price": 0})
    return prices

def read_transactions_from_json(file_path: str = "data/operations.json") -> list:
    """Загружает транзакции из JSON-файла."""
    path = Path(file_path)
    if not path.exists():
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Убедись, что данные — это список
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, IOError):
        return []
import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()

EXCHANGE_API_KEY = os.getenv("EXCHANGE_API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/latest"


def get_exchange_rate(from_currency: str, to_currency: str = "RUB") -> float:
    """
    Получает курс обмена через API.
    """
    headers = {"apikey": EXCHANGE_API_KEY}
    params = {"base": from_currency, "symbols": to_currency}

    response = requests.get(BASE_URL, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    return float(data["rates"][to_currency])  # Явное приведение к float


def convert_transaction_amount(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.
    """
    amount = float(transaction.get("amount", 0))
    currency_code = transaction.get("currency", {}).get("code", "RUB")

    if currency_code == "RUB":
        return amount
    elif currency_code in ("USD", "EUR"):
        rate = get_exchange_rate(currency_code)
        return amount * rate
    else:
        return 0.0

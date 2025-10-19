# src/views.py
import pandas as pd
import json
import logging
from src.utils import get_greeting, get_currency_rates, get_stock_prices

logger = logging.getLogger(__name__)


def get_main_page_data(date_str: str) -> str:
    """
    Возвращает JSON для главной страницы.

    Args:
        date_str: Дата в формате "YYYY-MM-DD HH:MM:SS"

    Returns:
        JSON-строка с данными.
    """
    logger.info("Генерация данных для главной страницы")

    # 1. Приветствие
    greeting = get_greeting(date_str)

    # 2. Загрузка транзакций
    from src.file_reader import load_transactions
    transactions = load_transactions()

    # Фильтрация по дате (с начала месяца до date_str)
    target_date = datetime.strptime(date_str.split()[0], "%Y-%m-%d")
    start_of_month = target_date.replace(day=1)

    filtered = [
        t for t in transactions
        if "Дата операции" in t and pd.to_datetime(t["Дата операции"]) >= start_of_month
           and pd.to_datetime(t["Дата операции"]) <= target_date
    ]

    # 2. Карты и кешбэк
    cards = {}
    for t in filtered:
        card = str(t.get("Номер карты", ""))[-4:]
        amount = t.get("Сумма операции", 0)
        if amount > 0:  # расходы
            cards.setdefault(card, 0)
            cards[card] += amount

    cards_list = [
        {
            "last_digits": card,
            "total_spent": round(spent, 2),
            "cashback": round(spent / 100, 2)
        }
        for card, spent in cards.items()
    ]

    # 3. Топ-5 транзакций
    top_transactions = sorted(
        filtered,
        key=lambda x: x.get("Сумма операции", 0),
        reverse=True
    )[:5]

    top_list = [
        {
            "date": t.get("Дата операции", "").split(" ")[0],
            "amount": t.get("Сумма операции", 0),
            "category": t.get("Категория", ""),
            "description": t.get("Описание", "")
        }
        for t in top_transactions
    ]

    # 4. Курсы и акции
    with open("user_settings.json", "r", encoding="utf-8") as f:
        settings = json.load(f)

    currency_rates = get_currency_rates(settings["user_currencies"])
    stock_prices = get_stock_prices(settings["user_stocks"])

    result = {
        "greeting": greeting,
        "cards": cards_list,
        "top_transactions": top_list,
        "currency_rates": currency_rates,
        "stock_prices": stock_prices
    }

    return json.dumps(result, ensure_ascii=False, indent=2)

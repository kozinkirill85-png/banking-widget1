# tests/test_services.py
from src.services import simple_search, search_phone_numbers

def test_simple_search():
    transactions = [{"Описание": "Покупка в Ленте", "Категория": "Супермаркеты"}]
    result = simple_search("лента", transactions)


def test_search_phone_numbers():
    transactions = [{"Описание": "Перевод +7 921 11-22-33"}]
    result = search_phone_numbers(transactions)
    assert "+7 921" in result

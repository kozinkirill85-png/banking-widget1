# src/services.py
import json
import re

def simple_search(query: str, transactions: list) -> str:
    """Простой поиск по описанию и категории."""
    result = []
    for t in transactions:
        # Поддерживаем оба варианта написания
        desc = str(t.get("Описание") or t.get("описание") or "")
        cat = str(t.get("Категория") or t.get("категория") or "")
        if query.lower() in desc.lower() or query.lower() in cat.lower():
            result.append(t)
    return json.dumps(result, ensure_ascii=False, indent=2)

def search_phone_numbers(transactions: list) -> str:
    # Поддерживаем: +7 921 11-22-33, +7921112233, +7 (921) 11-22-33
    phone_pattern = re.compile(r"\+7\s?[\d\s\-(\)]{10,}")
    result = [
        t for t in transactions
        if phone_pattern.search(str(t.get("Описание") or t.get("описание") or ""))
    ]
    return json.dumps(result, ensure_ascii=False, indent=2)

def test_simple_search():
    transactions = [{"Описание": "Покупка в Ленте", "Категория": "Супермаркеты"}]
    result = simple_search("лента", transactions)
    assert "Ленте" in result
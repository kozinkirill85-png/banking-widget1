import pytest
from src.processing import process_bank_search, process_bank_operations


def test_process_bank_search():
    data = [
        {"description": "Перевод на карту"},
        {"description": "Оплата за интернет"},
        {"description": "Покупка в магазине"},
    ]

    result = process_bank_search(data, "перевод")
    assert len(result) == 1
    assert result[0]["description"] == "Перевод на карту"

    result = process_bank_search(data, "оплата")
    assert len(result) == 1
    assert result[0]["description"] == "Оплата за интернет"

    result = process_bank_search(data, "")
    assert len(result) == 3

    result = process_bank_search(data, "не существует")
    assert len(result) == 0


def test_process_bank_operations():
    data = [
        {"description": "Перевод на карту"},
        {"description": "Оплата за интернет"},
        {"description": "Перевод на карту"},
        {"description": "Покупка в магазине"},
    ]
    categories = ["Перевод на карту", "Оплата за интернет", "Неизвестная категория"]

    result = process_bank_operations(data, categories)
    assert result["Перевод на карту"] == 2
    assert result["Оплата за интернет"] == 1
    assert result["Неизвестная категория"] == 0

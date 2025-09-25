# tests/test_generators.py

import pytest

from src.generators.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "description": "Перевод организации",
            "operationAmount": {"amount": "1000.00", "currency": {"code": "USD"}},
        },
        {
            "id": 2,
            "description": "Перевод со счета на счет",
            "operationAmount": {"amount": "500.00", "currency": {"code": "EUR"}},
        },
        {"id": 3, "description": "Оплата услуг", "operationAmount": {"amount": "200.00", "currency": {"code": "USD"}}},
        {
            "id": 4,
            "description": None,  # Проверка обработки None
            "operationAmount": {"amount": "1500.00", "currency": {"code": "RUB"}},
        },
        {
            "id": 5,
            "description": "Покупка акций",
            "operationAmount": {"amount": "1500.00", "currency": {"code": "USD"}},
        },
    ]


def test_filter_by_currency_usd(sample_transactions):
    usd_gen = filter_by_currency(sample_transactions, "USD")
    usd_list = list(usd_gen)
    assert len(usd_list) == 3
    assert usd_list[0]["id"] == 1
    assert usd_list[1]["id"] == 3
    assert usd_list[2]["id"] == 5


def test_filter_by_currency_empty():
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_transaction_descriptions(sample_transactions):
    desc_gen = transaction_descriptions(sample_transactions)
    descriptions = list(desc_gen)
    assert descriptions[0] == "Перевод организации"
    assert descriptions[1] == "Перевод со счета на счет"
    assert descriptions[2] == "Оплата услуг"
    assert descriptions[3] == "Описание отсутствует"  # из-за None
    assert descriptions[4] == "Покупка акций"


def test_transaction_descriptions_empty():
    descriptions = list(transaction_descriptions([]))
    assert descriptions == []


def test_card_number_generator_single():
    gen = card_number_generator(1, 1)
    assert next(gen) == "0000 0000 0000 0001"


def test_card_number_generator_range():
    gen = card_number_generator(1, 3)
    cards = list(gen)
    assert cards == ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]


def test_card_number_generator_invalid_range():
    with pytest.raises(ValueError):
        list(card_number_generator(-1, 10))


def test_card_number_generator_large():
    gen = card_number_generator(9999999999999998, 9999999999999999)
    cards = list(gen)
    assert cards == ["9999 9999 9999 9998", "9999 9999 9999 9999"]

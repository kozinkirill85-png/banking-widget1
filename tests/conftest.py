import pytest
from typing import Any




@pytest.fixture
def sample_operations() -> list[dict[str, Any]]:
    """Фикстура: список операций для тестов."""
    return [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "100.00",
                "currency": {
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678937855640"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "100.00",
                "currency": {
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 96527012345678901234",
            "to": "Счет 64686473678937855640"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "100.00",
                "currency": {
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Platinum 7000792289606361",
            "to": "Счет 64686473678937855640"
        },
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
            "operationAmount": {
                "amount": "100.00",
                "currency": {
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Gold 5999414228426354",
            "to": "Счет 64686473678937855640"
        }
    ]


@pytest.fixture
def empty_operations() -> list[dict[str, Any]]:
    """Фикстура: пустой список операций."""
    return []

import pytest
from typing import Any



@pytest.fixture
def sample_operations() -> list[dict[str, Any]]:
    return [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод организации"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"currency": {"code": "RUB"}},
            "description": "Перевод со счета на счет"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод с карты на карту"
        }
    ]

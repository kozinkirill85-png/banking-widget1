from unittest.mock import patch

from src.external_api import convert_transaction_amount


@patch("src.external_api.get_exchange_rate", return_value=90.0)
def test_convert_usd_to_rub(mock_get_rate) -> None:
    transaction = {
        "amount": 100,
        "currency": {"code": "USD"}
    }
    result = convert_transaction_amount(transaction)
    assert result == 9000.0
    mock_get_rate.assert_called_once_with("USD")


@patch("src.external_api.get_exchange_rate", return_value=100.0)
def test_convert_eur_to_rub(mock_get_rate) -> None:
    transaction = {
        "amount": 50,
        "currency": {"code": "EUR"}
    }
    result = convert_transaction_amount(transaction)
    assert result == 5000.0
    mock_get_rate.assert_called_once_with("EUR")


def test_convert_rub() -> None:
    transaction = {
        "amount": 200,
        "currency": {"code": "RUB"}
    }
    result = convert_transaction_amount(transaction)
    assert result == 200.0

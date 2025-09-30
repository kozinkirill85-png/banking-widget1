"""Тесты для функций модуля widget."""

import pytest

from src.widget import get_date, mask_account_card


# Тесты для mask_account_card
def test_mask_account_card_card() -> None:
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"


def test_mask_account_card_account() -> None:
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
    assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"


def test_mask_account_card_invalid() -> None:
    with pytest.raises(ValueError):
        mask_account_card("Invalid")
    with pytest.raises(ValueError):
        mask_account_card("Card abc123")


# Тесты для get_date
<<<<<< feature/decorators-log
def test_get_date():
=======
def test_get_date() -> None:
>>>>> develop
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2018-07-11T02:26:18") == "11.07.2018"
    assert get_date("2020-12-31T23:59:59.999999") == "31.12.2020"


def test_get_date_invalid() -> None:
    with pytest.raises(ValueError):
        get_date("invalid-date")
    with pytest.raises(ValueError):
        get_date("")

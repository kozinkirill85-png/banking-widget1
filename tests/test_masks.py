# tests/test_masks.py

import pytest
from typing import Union
from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        (7000792289606361, "7000 79** **** 6361"),
        ("1234567890123456", "1234 56** **** 3456"),
    ],
)
def test_get_mask_card_number(card_number: Union[int, str], expected: str) -> None:
    """Параметризованный тест для маскировки номера карты."""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        (73654108430135874305, "**4305"),
        ("1234567890", "**7890"),
    ],
)
def test_get_mask_account(account_number: Union[int, str], expected: str) -> None:
    """Параметризованный тест для маскировки номера счёта."""
    assert get_mask_account(account_number) == expected


def test_get_mask_card_number_invalid() -> None:
    """Тест на ошибку при неверной длине номера карты."""
    with pytest.raises(ValueError, match="Номер карты должен содержать ровно 16 цифр."):
        get_mask_card_number("12345")


def test_get_mask_account_invalid() -> None:
    """Тест на ошибку при нечисловом номере счёта."""
    with pytest.raises(ValueError, match="Номер счёта должен содержать только цифры."):
        get_mask_account("abc123")

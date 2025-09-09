"""Модуль для маскировки номеров карт и счетов."""

from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Возвращает маскированный номер карты в формате XXXX XX** **** XXXX.

    Args:
        card_number: Номер карты (16 цифр).

    Returns:
        Маскированная строка.
    """
    card_str = str(card_number).strip()
    if len(card_str) != 16 or not card_str.isdigit():
        raise ValueError("Номер карты должен содержать ровно 16 цифр.")
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: Union[int, str]) -> str:
    """Возвращает маскированный номер счёта в формате **XXXX.

    Args:
        account_number: Номер счёта.

    Returns:
        Маскированная строка.
    """
    acc_str = str(account_number).strip()
    if not acc_str.isdigit():
        raise ValueError("Номер счёта должен содержать только цифры.")
    return f"**{acc_str[-4:]}"

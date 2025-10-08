"""Модуль для маскировки номеров карт и счетов."""

import logging
from pathlib import Path
from typing import Union
from logging import Logger

# Создаем логер для модуля masks
logger: Logger = logging.getLogger(__name__)


# Настройка handler'а
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)
log_file = log_dir / "masks.log"

file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")

# Формат
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)

# Добавляем handler
logger.addHandler(file_handler)

# Уровень
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Возвращает маскированный номер карты в формате XXXX XX** **** XXXX.

    Args:
        card_number: Номер карты (16 цифр).

    Returns:
        Маскированная строка.
    """


    card_str = str(card_number).strip()
    if len(card_str) != 16 or not card_str.isdigit():
        logger.error(f"Неверный номер карты: '{card_number}'")
        raise ValueError("Номер карты должен содержать ровно 16 цифр.")

# Объявляем masked до return
    masked = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:]}"
    logger.debug(f"Маскировка карты: {card_number} -> {masked}")
    return masked


def get_mask_account(account_number: Union[int, str]) -> str:
    """Возвращает маскированный номер счёта в формате **XXXX.

    Args:
        account_number: Номер счёта.

    Returns:
        Маскированная строка.
    """
    acc_str = str(account_number).strip()
    if not acc_str.isdigit():
        logger.error(f"Неверный номер счета: '{account_number}'")
        raise ValueError("Номер счёта должен содержать только цифры.")

    masked = f"**{acc_str[-4:]}"
    logger.debug(f"Маскировка счета: {account_number} -> {masked}")
    return masked

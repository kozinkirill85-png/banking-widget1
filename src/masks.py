"""Модуль для маскировки номеров карт и счетов."""

import logging
from pathlib import Path
from typing import Union
from logging import Logger
from typing import Generator

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
    """Возвращает маскированный номер карты в формате XXXX XX** **** XXXX."""
    card_str = str(card_number)
    if len(card_str) != 16:
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
        logger.error(f"Неверный номер счета: '{account_number}'")
        raise ValueError("Номер счёта должен содержать только цифры.")

    masked = f"**{acc_str[-4:]}"
    logger.debug(f"Маскировка счета: {account_number} -> {masked}")
    return masked


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    if start > end or start < 0 or end > 9999999999999999:
        raise ValueError("Неверный диапазон номеров карт.")
    for num in range(start, end + 1):
        card_str = str(num).zfill(16)
        formatted = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:]}"
        yield formatted
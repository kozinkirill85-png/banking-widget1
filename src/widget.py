"""Модуль для обработки данных банковских операций."""

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """Маскирует номер карты или счёта в строке, оставляя тип без изменений.

    Примеры:
        "Visa Platinum 7000792289606361" → "Visa Platinum 7000 79** **** 6361"
        "Счет 73654108430135874305" → "Счет **4305"

    Args:
        info: Строка, содержащая тип (например, "Visa Classic", "Счет") и номер.

    Returns:
        Строка с замаскированным номером.
    """
    if not info or not info.strip():
        raise ValueError("Строка не должна быть пустой.")

    # Разделяем строку — последнее слово всегда номер
    parts = info.strip().rsplit(" ", 1)
    if len(parts) != 2:
        raise ValueError("Некорректный формат строки. Ожидается 'Тип Номер'.")

    name_part, number_part = parts

    if not number_part.isdigit():
        raise ValueError("Номер должен содержать только цифры.")

    if "Счет" in name_part:
        masked_number = get_mask_account(number_part)
    else:
        masked_number = get_mask_card_number(number_part)

    return f"{name_part} {masked_number}"


def get_date(date_string: str) -> str:
    """Преобразует строку даты в формат ДД.ММ.ГГГГ.

    Пример:
        "2024-03-11T02:26:18.671407" → "11.03.2024"

    Args:
        date_string: Дата в формате ISO (YYYY-MM-DDTHH:MM:SS.ffffff).

    Returns:
        Дата в формате "ДД.ММ.ГГГГ".
    """
    from datetime import datetime

    try:
        dt = datetime.fromisoformat(date_string.replace("Z", "+00:00").split(".")[0])
        return dt.strftime("%d.%m.%Y")
    except (ValueError, TypeError) as e:
        raise ValueError(f"Некорректный формат даты: {date_string}") from e

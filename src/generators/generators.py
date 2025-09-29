# src/generators/generators.py

from typing import Any, Dict, Iterator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """
    Фильтрует транзакции по указанной валюте.

    Args:
        transactions: Список транзакций (словарей).
        currency: Код валюты (например, 'USD').

    Yields:
        Транзакции, где валюта совпадает с заданной.
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Генератор, возвращающий описание каждой транзакции.

    Args:
        transactions: Список транзакций.

    Yields:
        Описание операции (строка). Если отсутствует или None — возвращает "Описание отсутствует".
    """
    for transaction in transactions:
        desc = transaction.get("description")
        if desc is None:
            yield "Описание отсутствует"
        else:
            yield str(desc)  # на случай, если вдруг не строка


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор номеров банковских карт в формате 'XXXX XXXX XXXX XXXX'.

    Args:
        start: Начальное значение (включительно).
        stop: Конечное значение (включительно).

    Yields:
        Строка с номером карты, отформатированная с пробелами.

    Raises:
        ValueError: Если start < 1 или stop > 9999999999999999.
    """
    if start < 1 or stop > 9999999999999999:
        raise ValueError("Номера карт должны быть в диапазоне от 1 до 9999999999999999")

    for num in range(start, stop + 1):
        card_str = f"{num:016d}"  # 16 цифр с ведущими нулями
        formatted = " ".join(card_str[i : i + 4] for i in range(0, 16, 4))
        yield formatted

# src/generators/generators.py

from typing import Any, Dict, Iterator, List, Generator


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Generator[Dict[str, Any], None, None]:
    """Генератор, возвращающий транзакции с указанной валютой."""
    for transaction in transactions:
        trans_currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")
        if trans_currency == currency:
            yield transaction

def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """Генератор, возвращающий описание каждой транзакции."""
    for transaction in transactions:
        desc = transaction.get("description")
        if desc is None:
            yield "Описание отсутствует"
        else:
            yield str(desc)


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    if start > end or start < 0 or end > 9999999999999999:
        raise ValueError("Неверный диапазон номеров карт.")
    for num in range(start, end + 1):
        card_str = str(num).zfill(16)
        formatted = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:]}"
        yield formatted

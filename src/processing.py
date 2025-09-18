# src/processing.py

from typing import Any, Dict, List


def filter_by_state(operations: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует операции по статусу.

    :param operations: Список словарей с операциями
    :param state: Статус для фильтрации (по умолчанию 'EXECUTED')
    :return: Новый список операций с заданным статусом
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(operations: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует операции по дате.

    :param operations: Список словарей с операциями
    :param reverse: Порядок сортировки (True — по убыванию, False — по возрастанию)
    :return: Новый отсортированный список
    """
    return sorted(operations, key=lambda x: x["date"], reverse=reverse)

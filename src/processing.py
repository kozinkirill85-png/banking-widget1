import re
from collections import Counter
from typing import List, Dict, Any


def process_bank_search(data: List[Dict[str, Any]], search: str) -> List[Dict[str, Any]]:
    """
    Функция поиска операций по строке в описании с использованием регулярных выражений.

    Args:
        data: Список словарей с данными о банковских операциях.
        search: Строка для поиска в поле 'description'.

    Returns:
        Список словарей, у которых в описании найдена строка.
    """
    if not search.strip():
        return data

    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [item for item in data if pattern.search(item.get("description", ""))]


def process_bank_operations(data: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Функция подсчёта количества операций по заданным категориям.

    Args:
        data: Список словарей с данными о банковских операциях.
        categories: Список категорий для подсчёта.

    Returns:
        Словарь, где ключ — категория, значение — количество операций.
    """
    # Извлекаем категории из description (или можно использовать другое поле)
    # Здесь предполагается, что category = description, но можно адаптировать
    descriptions = [item.get("description", "") for item in data]
    counter = Counter(descriptions)

    # Возвращаем только те категории, которые переданы в аргументе
    result = {cat: counter.get(cat, 0) for cat in categories}
    return result

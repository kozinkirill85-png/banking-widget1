# tests/test_processing.py

from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(sample_operations: List[Dict[str, Any]]) -> None:
    """Тест фильтрации по EXECUTED."""
    result = filter_by_state(sample_operations)
    assert len(result) == 2
    assert all(op["state"] == "EXECUTED" for op in result)


def test_filter_by_state_canceled(sample_operations: List[Dict[str, Any]]) -> None:
    """Тест фильтрации по CANCELED."""
    result = filter_by_state(sample_operations, "CANCELED")
    assert len(result) == 2
    assert all(op["state"] == "CANCELED" for op in result)


def test_filter_by_state_empty(empty_operations: List[Dict[str, Any]]) -> None:
    """Тест фильтрации пустого списка."""
    result = filter_by_state(empty_operations)
    assert result == []


@pytest.mark.parametrize(
    "reverse, first_id",
    [
        (True, 41428829),   # по убыванию — самая новая операция
        (False, 939719570),    # по возрастанию — самая старая
    ],
)
def test_sort_by_date(
    sample_operations: List[Dict[str, Any]],
    reverse: bool,
    first_id: int
) -> None:
    """Параметризованный тест сортировки."""
    result = sort_by_date(sample_operations, reverse=reverse)
    assert result[0]["id"] == first_id


def test_sort_by_date_empty(empty_operations: List[Dict[str, Any]]) -> None:
    """Тест сортировки пустого списка."""
    result = sort_by_date(empty_operations)
    assert result == []

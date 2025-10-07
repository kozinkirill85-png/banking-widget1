import json
from unittest.mock import mock_open, patch

from src.utils import read_transactions_from_json


def test_read_valid_json() -> None:
    data = [{"id": 1, "amount": 100}]
    with patch("src.utils.Path.exists", return_value=True):
        with patch("src.utils.open", mock_open(read_data=json.dumps(data))):
            result = read_transactions_from_json("fake_path.json")
    assert result == data


def test_file_not_found() -> None:
    with patch("src.utils.Path.exists", return_value=False):
        result = read_transactions_from_json("nonexistent.json")
    assert result == []


def test_invalid_json() -> None:
    with patch("src.utils.Path.exists", return_value=True):
        with patch("src.utils.open", mock_open(read_data="invalid json")):
            result = read_transactions_from_json("bad.json")
    assert result == []


def test_non_list_json() -> None:
    data = {"not": "a list"}
    with patch("src.utils.Path.exists", return_value=True):
        with patch("src.utils.open", mock_open(read_data=json.dumps(data))):
            result = read_transactions_from_json("fake_path.json")
    assert result == []

import pandas as pd
from unittest.mock import patch, Mock
from src.file_reader import read_transactions_from_csv, read_transactions_from_excel


@patch("pandas.read_csv")
def test_read_transactions_from_csv_success(mock_read_csv):
    # Подготавливаем данные
    mock_df = pd.DataFrame({
        "id": [1, 2],
        "amount": [100, 200],
        "currency": ["RUB", "USD"]
    })
    mock_read_csv.return_value = mock_df

    result = read_transactions_from_csv("fake.csv")

    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["amount"] == 200
    mock_read_csv.assert_called_once_with("fake.csv")


@patch("pandas.read_csv")
def test_read_transactions_from_csv_file_not_found(mock_read_csv):
    mock_read_csv.side_effect = FileNotFoundError
    result = read_transactions_from_csv("nonexistent.csv")
    assert result == []


@patch("pandas.read_excel")
def test_read_transactions_from_excel_success(mock_read_excel):
    mock_df = pd.DataFrame({
        "id": [3, 4],
        "amount": [300, 400],
        "currency": ["EUR", "RUB"]
    })
    mock_read_excel.return_value = mock_df

    result = read_transactions_from_excel("fake.xlsx")

    assert len(result) == 2
    assert result[0]["id"] == 3
    assert result[1]["currency"] == "RUB"
    mock_read_excel.assert_called_once_with("fake.xlsx")


@patch("pandas.read_excel")
def test_read_transactions_from_excel_file_not_found(mock_read_excel):
    mock_read_excel.side_effect = FileNotFoundError
    result = read_transactions_from_excel("nonexistent.xlsx")
    assert result == []

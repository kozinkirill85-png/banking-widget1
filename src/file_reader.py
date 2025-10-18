import json
import pandas as pd


def read_transactions_from_json(file_path: str) -> list:
    """Читает транзакции из JSON файла."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_transactions_from_csv(file_path: str) -> list:
    """Читает транзакции из CSV файла."""
    try:
        df = pd.read_csv(file_path)
        return df.to_dict("records")
    except (FileNotFoundError, pd.errors.EmptyDataError):
        return []


def read_transactions_from_excel(file_path: str) -> list:
    """Читает транзакции из XLSX файла."""
    try:
        df = pd.read_excel(file_path)
        return df.to_dict("records")
    except (FileNotFoundError, ValueError):
        return []

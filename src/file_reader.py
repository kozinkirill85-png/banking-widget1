import pandas as pd
from pathlib import Path
from typing import List, Dict, Any


def read_transactions_from_csv(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает финансовые транзакции из CSV-файла и возвращает список словарей.

    Args:
        file_path (str): Путь к CSV-файлу.

    Returns:
        List[Dict[str, Any]]: Список транзакций или пустой список при ошибке.
    """
    try:
        path = Path(file_path)
        if not path.exists():
            print(f"Файл {file_path} не найден.")
            return []

        df = pd.read_csv(path)
        # Преобразуем DataFrame в список словарей
        transactions = df.to_dict(orient="records")
        print(f"✅ Успешно прочитано {len(transactions)} транзакций из CSV.")
        return transactions

    except Exception as e:
        print(f"Ошибка при чтении CSV-файла {file_path}: {e}")
        return []


def read_transactions_from_excel(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает финансовые транзакции из Excel-файла (.xlsx) и возвращает список словарей.

    Args:
        file_path (str): Путь к Excel-файлу.

    Returns:
        List[Dict[str, Any]]: Список транзакций или пустой список при ошибке.
    """
    try:
        path = Path(file_path)
        if not path.exists():
            print(f"Файл {file_path} не найден.")
            return []

        df = pd.read_excel(path)
        transactions = df.to_dict(orient="records")
        print(f"✅ Успешно прочитано {len(transactions)} транзакций из Excel.")
        return transactions

    except Exception as e:
        print(f"Ошибка при чтении Excel-файла {file_path}: {e}")
        return []

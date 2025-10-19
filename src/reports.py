# src/reports.py
import json
import logging
from datetime import datetime, timedelta
from typing import Optional
import pandas as pd

logger = logging.getLogger(__name__)


def log_report(filename: str = None):
    """Декоратор для логирования отчётов."""

    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            fname = filename or f"report_{func.__name__}.json"
            with open(fname, "w", encoding="utf-8") as f:
                if isinstance(result, pd.DataFrame):
                    f.write(result.to_json(orient="records", indent=2, force_ascii=False))
                else:
                    json.dump(result, f, ensure_ascii=False, indent=2)
            logger.info(f"Отчёт сохранён в {fname}")
            return result

        return wrapper

    return decorator


@log_report()
def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """Траты по категории за последние 3 месяца."""
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    end_date = pd.to_datetime(date)
    start_date = end_date - timedelta(days=90)

    filtered = transactions[
        (transactions["Категория"] == category) &
        (pd.to_datetime(transactions["Дата операции"]) >= start_date) &
        (pd.to_datetime(transactions["Дата операции"]) <= end_date)
        ]
    return filtered

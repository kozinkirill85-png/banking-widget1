# 🏦 Banking Widget

Проект для обработки банковских операций: маскировка данных, фильтрация и сортировка.

## 📁 Структура

- `src/` — основной код
  - `masks.py` — маскировка номеров карт и счетов
  - `widget.py` — обработка строк и дат
  - `processing.py` — фильтрация и сортировка операций
- `tests/` — тесты

## 🛠️ Установка

Клонируйте репозиторий и используйте функции напрямую.

## 📚 Примеры

```python
from src.processing import filter_by_state, sort_by_date

operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}
]

executed = filter_by_state(operations)
sorted_ops = sort_by_date(operations)
 feature/homework_10_1
# 🏦 Banking Widget

Проект для обработки банковских операций: маскировка данных, фильтрация и сортировка.

## 📁 Структура проекта

- `src/` — основной код
  - `masks.py` — маскировка номеров карт и счетов
  - `widget.py` — обработка строк (маскировка, дата)
  - `processing.py` — фильтрация и сортировка операций
- `tests/` — модульные тесты

## 🚀 Начало работы

### Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-логин/banking-widget.git
   cd banking-widget
   

## 🧪 Тестирование

Проект покрыт тестами на 100%. Используются:

- `pytest` — для запуска тестов
- `pytest-cov` — для измерения покрытия
- Фикстуры и параметризация — для гибкости и избежания дублирования

### Как запустить тесты

```bash


pytest tests/ -v

My Homework
 develop
 
 
## Модуль `generators`

Модуль предоставляет генераторы для эффективной работы с большими объемами транзакций.

### Функции

#### `filter_by_currency(transactions, currency)`
Фильтрует транзакции по валюте.

**Пример:**
```python
from src.generators.generators import filter_by_currency

usd_ops = filter_by_currency(transactions, "USD")
for op in usd_ops:
    print(op['description'])
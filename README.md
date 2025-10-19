 feature/decorators-log

 feature/homework_10_1
 develop
# 🏦 Banking Widget

Проект для обработки банковских операций: маскировка данных, фильтрация и сортировка.

 feature/decorators-log

- `src/` — основной код
  - `masks.py` — маскировка номеров карт и счетов
  - `processing.py` — фильтрация и сортировка операций


```python
## Модуль `decorators`

Содержит декораторы для логирования выполнения функций.

### Декоратор `log(filename=None)`

Автоматически логирует вызовы функций: успешные и с ошибками.

#### Пример: логирование в файл

```python
from src.decorators.decorators import log

@log(filename="mylog.txt")
def add(a, b):
    return a + b

add(1, 2)  # Запишет в mylog.txt: "add ok"
=======
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
 develop
## Тестирование

Проект покрыт автоматизированными тестами с использованием библиотеки `pytest`.

### Запуск тестов

```bash
pytest tests/ -v

## Новая функциональность

Теперь проект поддерживает чтение данных о транзакциях из следующих форматов:
- JSON (уже было)
- CSV
- Excel (.xlsx)

Для работы с CSV и Excel требуется установка зависимостей:
```bash
pip install -r requirements.txt

# Курсовая работа: Анализ банковских транзакций

## Функционал
- Веб-страница «Главная» с приветствием, картами, топ-транзакциями, курсами и акциями.
- Сервисы: простой поиск, поиск по телефонам.
- Отчёты: траты по категории с логированием.

## Запуск
```bash
poetry install
python src/main.py
# 🏦 Banking Widget

Проект для обработки банковских операций: маскировка данных, фильтрация и сортировка.


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

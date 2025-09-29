# src/decorators/decorators.py

import functools
import sys
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования вызовов функций.

    Логирует:
    - Успешное выполнение: "<function_name> ok"
    - Ошибку: "<function_name> error: <error_type>. Inputs: (<args>), {<kwargs>}"

    Args:
        filename: Имя файла для записи логов. Если None — логи выводятся в консоль.

    Returns:
        Декорированную функцию.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                else:
                    print(message, file=sys.stdout)
                return result
            except Exception as e:
                error_type = type(e).__name__
                message = f"{func.__name__} error: {error_type}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                else:
                    print(message, file=sys.stderr)
                raise
        return wrapper
    return decorator

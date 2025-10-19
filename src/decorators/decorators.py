import sys
from functools import wraps
from typing import Callable, Any, Optional


def log(filename: str | None = None) -> Callable[..., Any]:
    """
    Декоратор для логирования вызовов функций.
    Если filename указан — пишет в файл, иначе — в консоль.
    """
    def decorator(func: Callable) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                msg = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(msg + "\n")
                else:
                    print(msg)
                return result
            except Exception as e:
                msg = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(msg + "\n")
                else:
                    print(msg, file=sys.stderr)
                raise
        return wrapper
    return decorator

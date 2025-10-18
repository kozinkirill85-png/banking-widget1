# tests/test_decorators.py

import os

import pytest

from src.decorators.decorators import log


# Тестовые функции
@log(filename="test_log.txt")
def my_function(x: int, y: int) -> int:
    return x + y


@log()
def my_function_console(x: int, y: int) -> int:
    return x + y


@log(filename="error_log.txt")
def my_function_error(x: int) -> None:
    if x < 0:
        raise ValueError("x must be non-negative")
    return None


def test_log_success_file():
    """Тест успешного выполнения с записью в файл."""
    log_file = "test_log.txt"
    if os.path.exists(log_file):
        os.remove(log_file)

    result = my_function(1, 2)
    assert result == 3

    with open(log_file, "r", encoding="utf-8") as f:
        log_content = f.read().strip()

    assert log_content == "my_function ok"

    os.remove(log_file)  # Теперь работает!


def test_log_success_console(capsys):
    """Тест успешного выполнения с выводом в консоль."""
    result = my_function_console(3, 4)
    assert result == 7

    captured = capsys.readouterr()
    assert captured.out.strip() == "my_function_console ok"


def test_log_error_file():
    """Тест ошибки с записью в файл."""
    log_file = "error_log.txt"
    if os.path.exists(log_file):
        os.remove(log_file)

    with pytest.raises(ValueError):
        my_function_error(-1)

    with open(log_file, "r", encoding="utf-8") as f:
        log_content = f.read().strip()

    assert log_content == "my_function_error error: ValueError. Inputs: (-1,), {}"

    os.remove(log_file)


def test_log_error_console(capsys):
    """Тест ошибки с выводом в консоль."""
    @log()
    def func_with_error():
        raise RuntimeError("Something went wrong")

    with pytest.raises(RuntimeError):
        func_with_error()

    captured = capsys.readouterr()
    assert "func_with_error error: RuntimeError. Inputs: (), {}" in captured.err

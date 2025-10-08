import logging
from pathlib import Path



# Создаем логер для модуля utils
logger = logging.getLogger(__name__)

# Настройка handler'а для записи в файл
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)  # Создаем папку, если её нет
log_file = log_dir / "utils.log"

file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")  # 'w' — перезапись при каждом запуске

# Формат лога: время, модуль, уровень, сообщение
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)

# Добавляем handler к логеру
logger.addHandler(file_handler)

# Устанавливаем уровень логирования
logger.setLevel(logging.DEBUG)

import json
from pathlib import Path
from typing import Any, Dict, List


def read_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл с транзакциями и возвращает список словарей.
    Если файл не найден, пустой или содержит не список — возвращает пустой список.

    Args:
        file_path (str): Путь к JSON-файлу.

    Returns:
        List[Dict[str, Any]]: Список транзакций или пустой список.
    """
    try:
        path = Path(file_path)
        if not path.exists():
            logger.error(f"Файл {file_path} не найден.")
            return []

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, list):
            logger.debug(f"Успешно прочитано {len(data)} транзакций из файла {file_path}.")
            return data
        else:
            logger.error(f"Данные в файле {file_path} не являются списком.")
            return []
    except (json.JSONDecodeError, IOError) as e:
        logger.error(f"Ошибка при чтении файла {file_path}: {e}")
        return []

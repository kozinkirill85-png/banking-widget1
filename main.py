import json
import os
from datetime import datetime
from src.file_reader import read_transactions_from_csv, read_transactions_from_csv, read_transactions_from_excel
from src.processing import process_bank_search, process_bank_operations


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input().strip()

    if choice == "1":
        file_path = "data/operations.json"
        if not os.path.exists(file_path):
            print("Файл operations.json не найден.")
            return
        transactions = read_transactions_from_csv(file_path)
        print("Для обработки выбран JSON-файл.")
    elif choice == "2":
        file_path = "data/operations.csv"
        if not os.path.exists(file_path):
            print("Файл operations.csv не найден.")
            return
        transactions = read_transactions_from_csv(file_path)
        print("Для обработки выбран CSV-файл.")
    elif choice == "3":
        file_path = "data/operations.xlsx"
        if not os.path.exists(file_path):
            print("Файл operations.xlsx не найден.")
            return
        transactions = read_transactions_from_excel(file_path)
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Неверный выбор.")
        return

    # Фильтрация по статусу
    valid_statuses = {"EXECUTED", "CANCELED", "PENDING"}
    while True:
        status_input = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        ).strip().upper()
        if status_input in valid_statuses:
            filtered = [t for t in transactions if t.get("status", "").upper() == status_input]
            print(f"Операции отфильтрованы по статусу \"{status_input}\"")
            break
        else:
            print(f"Статус операции \"{status_input}\" недоступен.")

    # Отсортировать по дате?
    sort_by_date = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
    if sort_by_date in ("да", "yes", "y"):
        order = input("Отсортировать по возрастанию или по убыванию?\n").strip()
        reverse = order == "по убыванию"
        try:
            filtered.sort(key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=reverse)
        except (KeyError, ValueError):
            print("Ошибка при сортировке по дате — формат даты не соответствует ожидаемому.")

    # Только рублевые?
    rub_only = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower()
    if rub_only in ("да", "yes", "y"):
        filtered = [t for t in filtered if t.get("currency", {}).get("name") == "руб."]

    # Поиск по описанию
    search_desc = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower()
    if search_desc in ("да", "yes", "y"):
        search_term = input("Введите слово для поиска:\n").strip()
        filtered = process_bank_search(filtered, search_term)

    # Вывод результата
    print("\nРаспечатываю итоговый список транзакций...\n")
    if not filtered:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"Всего банковских операций в выборке: {len(filtered)}\n")

    for transaction in filtered:
        date_str = transaction.get("date", "").split("T")[0] if "date" in transaction else "Неизвестно"
        description = transaction.get("description", "Без описания")
        from_account = transaction.get("from", "Не указан")
        to_account = transaction.get("to", "Не указан")
        amount = transaction.get("operationAmount", {}).get("amount", "0")
        currency = transaction.get("operationAmount", {}).get("currency", {}).get("name", "N/A")

        print(f"{date_str} {description}")
        print(f"{from_account} -> {to_account}")
        print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()

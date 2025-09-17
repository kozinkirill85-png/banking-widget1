"""Демонстрация работы функций маскировки."""

from src.masks import get_mask_account, get_mask_card_number


def main() -> None:
    card = 7000792289606361
    account = 73654108430135874305

    print("Маска карты:", get_mask_card_number(card))
    print("Маска счёта:", get_mask_account(account))


if __name__ == "__main__":
    main()

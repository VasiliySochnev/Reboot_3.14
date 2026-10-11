from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(coming_str: Union[str]) -> Union[str]:
    """Функция, которая возвращает исходную строку
    с замаскированным номером карты/счета"""

    new_coming_str = coming_str.split()
    mask_number = ""
    for simbol in new_coming_str:
        if simbol.isalpha():
            mask_number += simbol + " "
        elif simbol.isdigit() and len(simbol) == 16:
            mask_number += get_mask_card_number(simbol) + " "
        elif simbol.isdigit() and len(simbol) == 20:
            mask_number += get_mask_account(simbol) + " "
    return mask_number.strip()


def get_date(date: str) -> str:
    """Функция, которая конвертирует дату из формата
    гггг.мм.дд в формат дд.мм.гггг"""

    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


#
# def main():
#     coming_str = 'Счет 64686473678894779589'
#     amount = mask_account_card(coming_str)
#     print(amount)
#
# # Это "магическая" проверка
# if __name__ == "__main__":
#     main()

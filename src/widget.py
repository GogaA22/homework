from datetime import datetime
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(number_card: str) -> str:
    number_card_list = number_card.split()
    number = number_card_list.pop()
    name = " ".join(number_card_list)
    if "Счет" in number_card:
        return f"Счет {get_mask_account(number)}"
    else:
        return f"{name} {get_mask_card_number(number)}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ.
    """
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")

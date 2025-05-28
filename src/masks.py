def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты: показывает первые 6 и последние 4 цифры.
    Пример: 7000792289606361 -> 7000 79** **** 6361
    """
    cleaned = card_number.replace(" ", "")
    if len(cleaned) != 16 or not cleaned.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр.")
    return f"{cleaned[:4]} {cleaned[4:6]}** **** {cleaned[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета: показывает только последние 4 цифры.
    Пример: 73654108430135874305 -> **4305
    """
    cleaned = account_number.replace(" ", "")
    if len(cleaned) < 4 or not cleaned.isdigit():
        raise ValueError("Номер счета должен содержать как минимум 4 цифры.")
    return f"**{cleaned[-4:]}"

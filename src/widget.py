from datetime import datetime









def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ.
    """
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")


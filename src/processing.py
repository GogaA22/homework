from typing import List, Dict


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список операций по значению поля 'state'.

    :param data: Список словарей с операциями
    :param state: Значение, по которому нужно фильтровать (по умолчанию 'EXECUTED')
    :return: Новый список только с операциями нужного статуса
    """
    filtered = []
    for item in data:
        if item.get("state") == state:
            filtered.append(item)
    return filtered


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список операций по дате.

    :param data: Список словарей с операциями
    :param reverse: True — сортировка от новых к старым, False — от старых к новым
    :return: Новый отсортированный список
    """

    return sorted(data, key=lambda item: item["date"], reverse=reverse)

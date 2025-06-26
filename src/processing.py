from typing import List, Dict
from datetime import datetime

def sort_by_date(data: List[Dict[str, str]], is_descending: bool = True) -> List[Dict[str, str]]:
   """
   Сортирует список операций по дате (ISO-формат -> datetime).
   :param data: Список словарей с операциями
   :param is_descending: True — сортировка от новых к старым, False — от старых к новым
   :return: Отсортированный список операций
   """
   return sorted(
     data,
     key=lambda item: datetime.fromisoformat(item["date"]),
     reverse=is_descending
   )
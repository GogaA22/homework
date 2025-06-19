from typing import List, Dict
from datetime import datetime


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    return sorted(data, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)
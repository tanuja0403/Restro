import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / 'data'
ORDERS_JSON = DATA_DIR / 'orders.json'


def load_orders():
    if not ORDERS_JSON.exists():
        return []
    with open(ORDERS_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_order(order):
    orders = load_orders()
    orders.append(order)
    with open(ORDERS_JSON, 'w', encoding='utf-8') as f:
        json.dump(orders, f, indent=2)
    return order


def clear_orders():
    with open(ORDERS_JSON, 'w', encoding='utf-8') as f:
        json.dump([], f)
    return []

import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / 'data'
INVENTORY_JSON = DATA_DIR / 'inventory.json'


def _load():
    if not INVENTORY_JSON.exists():
        return {}
    with open(INVENTORY_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)


def _save(d):
    with open(INVENTORY_JSON, 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2)


def get_inventory():
    return _load()


def update_item(name, delta):
    d = _load()
    d[name] = d.get(name, 0) + delta
    _save(d)
    return d[name]


def set_item(name, amount):
    d = _load()
    d[name] = amount
    _save(d)
    return amount

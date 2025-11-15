import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / 'data'
MENU_JSON = DATA_DIR / 'menu.json'


def load_menu():
    if not MENU_JSON.exists():
        return []
    with open(MENU_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_item(item_id):
    menu = load_menu()
    for item in menu:
        if item.get('id') == item_id:
            return item
    return None


def list_menu():
    return load_menu()

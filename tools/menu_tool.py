# import json
# import os

# def load_menu():
#     """Load menu data from menu.json"""
#     path = os.path.join("data", "menu.json")
#     with open(path, "r") as f:
#         return json.load(f)

# def search_menu(query):
#     """Search menu items by keyword"""
#     menu = load_menu()
#     query = query.lower()

#     results = []
#     for item in menu:
#         if query in item["name"].lower() or query in item["category"].lower():
#             results.append(item)

#     return results

# def filter_menu(veg=None, spicy=None):
#     """Filter menu based on veg/spicy preferences"""
#     menu = load_menu()
#     results = []

#     for item in menu:
#         if veg is not None and item["veg"] != veg:
#             continue
#         if spicy is not None and item["spicy"] != spicy:
#             continue
#         results.append(item)

#     return results



import json
import os

def load_menu():
    """Load menu data from menu.json"""
    path = os.path.join("data", "menu.json")
    with open(path, "r") as f:
        return json.load(f)

def search_menu(query):
    """Search menu items by keyword"""
    menu = load_menu()
    query = query.lower()

    results = []
    for item in menu:
        if query in item["name"].lower() or query in item["category"].lower():
            results.append(item)

    return results

def filter_menu(veg=None, spicy=None):
    """Filter menu based on veg/spicy preferences"""
    menu = load_menu()
    results = []

    for item in menu:
        if veg is not None and item["veg"] != veg:
            continue
        if spicy is not None and item["spicy"] != spicy:
            continue
        results.append(item)

    return results


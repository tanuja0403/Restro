from tools.inventory_tool import get_inventory, set_item


class ManagerAgent:
    def view_inventory(self):
        return get_inventory()

    def set_stock(self, item_name, amount):
        return set_item(item_name, amount)

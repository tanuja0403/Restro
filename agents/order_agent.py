import uuid
import datetime
from tools.order_db_tool import save_order
from tools.menu_tool import get_item


class OrderAgent:
    def create_order(self, item_id, quantity=1, customer=None):
        item = get_item(item_id)
        if not item:
            raise ValueError(f"Menu item {item_id} not found")

        order = {
            'order_id': str(uuid.uuid4()),
            'item_id': item_id,
            'item_name': item['name'],
            'quantity': quantity,
            'price': item['price'] * quantity,
            'customer': customer or 'guest',
            'created_at': datetime.datetime.utcnow().isoformat() + 'Z'
        }
        save_order(order)
        return order

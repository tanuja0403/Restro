# from agents.menu_agent import MenuAgent
# from agents.order_agent import OrderAgent
# from agents.reservation_agent import ReservationAgent
# from agents.manager_agent import ManagerAgent


# class RestaurantController:
#     def __init__(self):
#         self.menu_agent = MenuAgent()
#         self.order_agent = OrderAgent()
#         self.reservation_agent = ReservationAgent()
#         self.manager_agent = ManagerAgent()

#     def start(self):
#         # very small CLI to exercise agents
#         print(self.menu_agent.display_menu())
#         print('Commands: order <item_id> <qty> | reserve <name> <time> | inventory | quit')

#         while True:
#             cmd = input('> ').strip()
#             if cmd == 'quit':
#                 print('Goodbye!')
#                 break
#             parts = cmd.split()
#             if not parts:
#                 continue

#             if parts[0] == 'order' and len(parts) >= 2:
#                 item_id = parts[1]
#                 qty = int(parts[2]) if len(parts) >= 3 else 1
#                 order = self.order_agent.create_order(item_id, qty)
#                 print('Order Created:')
#                 print(order)
#             elif parts[0] == 'reserve' and len(parts) >= 3:
#                 name = parts[1]
#                 time = ' '.join(parts[2:])
#                 res = self.reservation_agent.create_reservation(name, time)
#                 print('Reservation made:')
#                 print(res)
#             elif parts[0] == 'inventory':
#                 inv = self.manager_agent.view_inventory()
#                 print('Inventory:')
#                 print(inv)
#             else:
#                 print('Unknown command')

from agents.menu_agent import MenuAgent

class ControllerAgent:

    def __init__(self):
        self.menu_agent = MenuAgent()

    def route(self, user_message):
        msg = user_message.lower()

        # broader matching for menu
        if any(keyword in msg for keyword in [
            "menu", "show", "find", "dish", "food",
            "veg", "non veg", "non-veg",
            "spicy", "starter", "breakfast", "biryani",
            "rice", "dosa", "paneer"
        ]):
            return self.menu_agent.handle(msg)

        return "I'm not sure what you mean. Try asking about the menu!"

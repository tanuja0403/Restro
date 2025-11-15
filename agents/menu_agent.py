from tools.menu_tool import search_menu, filter_menu
import json

class MenuAgent:

    def handle(self, user_message, memory=None):
        user_message = user_message.lower()

        # Search by keyword
        if "show" in user_message or "find" in user_message:
            # Example: "show biryani" or "find dosa"
            keyword = user_message.replace("show", "").replace("find", "").strip()
            results = search_menu(keyword)
            return self.format_results(results)

        # Veg filter
        if "veg" in user_message:
            results = filter_menu(veg=True)
            return self.format_results(results)

        # Non-veg filter
        if "non veg" in user_message or "non-veg" in user_message:
            results = filter_menu(veg=False)
            return self.format_results(results)

        # Spicy filter
        if "spicy" in user_message:
            results = filter_menu(spicy="medium")
            return self.format_results(results)

        return "I can help with menu searches! Try: 'show veg items', 'find dosa', or 'show spicy dishes'."

    def format_results(self, items):
        if not items:
            return "No items found!"

        response = "Here are the items:\n"
        for i in items:
            response += f"- {i['name']} (₹{i['price']}) — {i['category']}\n"
        return response

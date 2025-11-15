from tools.menu_tool import list_menu


class MenuAgent:
    """Agent to provide menu info."""

    def get_menu(self):
        return list_menu()

    def display_menu(self):
        menu = self.get_menu()
        text = "Today's Menu:\n"
        for item in menu:
            text += f" - {item['id']}: {item['name']} (${item['price']}) - {item.get('description', '')}\n"
        return text

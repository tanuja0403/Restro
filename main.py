# from agents.controller import RestaurantController


# if __name__ == "__main__":
#     controller = RestaurantController()
#     controller.start()


from agents.controller import ControllerAgent

controller = ControllerAgent()

while True:
    msg = input("You: ")
    response = controller.route(msg)
    print("Agent:", response)

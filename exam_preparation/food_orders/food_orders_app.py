from food_orders.client import Client
from food_orders.meals.meal import Meal


class FoodOrdersApp:
    RECEIPT_ID = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def __check_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def __check_client(self, phone_number: str):
        for client in self.clients_list:
            if client.phone_number == phone_number:
                return True

    def __client(self, phone_number: str):
        for client in self.clients_list:
            if client.phone_number == phone_number:
                return client

    def register_client(self, client_phone_number: str):
        if self.__check_client(client_phone_number):
            raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if isinstance(meal, Meal):
                self.menu.append(meal)

    def show_menu(self):
        self.__check_menu()
        menu = []

        for dish in self.menu:
            menu.append(dish.details())

        return '\n'.join(menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self.__check_menu()

        if not self.__check_client(client_phone_number):
            self.register_client(client_phone_number)

        ordered_meals_list = []
        client_bill = 0

        for meal_name, quantity in meal_names_and_quantities.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    if meal.quantity >= quantity:
                        ordered_meals_list.append(meal)
                        client_bill += quantity * meal.price
                        break
                    else:
                        raise Exception(f"Not enough quantity of {type(meal).__name__}: {meal_name}!")

            else:
                raise Exception(f"{meal_name} is not on the menu!")

        client = self.__client(client_phone_number)

        client.shopping_cart.extend(ordered_meals_list)
        client.bill += client_bill

        for meal_name, quantity in meal_names_and_quantities.items():
            client.ordered_meals_dict[meal_name] = quantity
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity -= quantity

        meal_names = [meal.name for meal in client.shopping_cart]

        return f"Client {client_phone_number} successfully ordered {', '.join(meal_names)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.__client(client_phone_number)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal_name, quantity in client.ordered_meals_dict.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity += quantity

        client.ordered_meals_dict = {}
        client.shopping_cart = []
        client.bill = 0.0

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.__client(client_phone_number)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        total_paid_money = client.bill

        client.ordered_meals_dict = {}
        client.shopping_cart = []
        client.bill = 0.0

        self.RECEIPT_ID += 1

        return f"Receipt #{self.RECEIPT_ID} with total amount of {total_paid_money:.2f}" \
               f" was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

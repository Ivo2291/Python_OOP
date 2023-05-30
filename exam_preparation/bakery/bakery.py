from bakery.baked_food.bread import Bread
from bakery.baked_food.cake import Cake
from bakery.drink.tea import Tea
from bakery.drink.water import Water
from bakery.table.inside_table import InsideTable
from bakery.table.outside_table import OutsideTable


class Bakery:
    FOOD_TYPES = {
        "Bread": Bread,
        "Cake": Cake
    }

    DRINK_TYPES = {
        "Tea": Tea,
        "Water": Water
    }

    TABLE_TYPES = {
        "InsideTable": InsideTable,
        "OutsideTable": OutsideTable
    }

    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def __find_table(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table

    def __find_food(self, food_name):
        for food in self.food_menu:
            if food.name == food_name:
                return food

    def __find_drink(self, drink_name):
        for drink in self.drinks_menu:
            if drink.name == drink_name:
                return drink

    def add_food(self, food_type: str, name: str, price: float):
        for food_obj in self.food_menu:
            if food_obj.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type in self.FOOD_TYPES:
            food = self.FOOD_TYPES[food_type](name, price)
            self.food_menu.append(food)

            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        for drink_obj in self.drinks_menu:
            if drink_obj.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type in self.DRINK_TYPES:
            drink = self.DRINK_TYPES[drink_type](name, portion, brand)
            self.drinks_menu.append(drink)

            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        for table_obj in self.tables_repository:
            if table_obj.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type in self.TABLE_TYPES:
            table = self.TABLE_TYPES[table_type](table_number, capacity)
            self.tables_repository.append(table)

            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.is_reserved = True
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
            else:
                return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food):
        table = self.__find_table(table_number)
        if not table:
            return f"Could not find table {table_number}"

        ordered_food = [f"Table {table_number} ordered:"]
        not_in_the_menu = [f"{self.name} does not have in the menu:"]

        for food_name in food:
            current_food = self.__find_food(food_name)

            if current_food:
                ordered_food.append(current_food.__repr__())
                table.food_orders.append(current_food)
            else:
                not_in_the_menu.append(food_name)

        result = ordered_food + not_in_the_menu

        return "\n".join(result)

    def order_drink(self, table_number: int, *drinks):
        table = self.__find_table(table_number)
        if not table:
            return f"Could not find table {table_number}"

        ordered_drinks = [f"Table {table_number} ordered:"]
        not_in_the_menu = [f"{self.name} does not have in the menu:"]

        for drink_name in drinks:
            current_drink = self.__find_drink(drink_name)

            if current_drink:
                ordered_drinks.append(current_drink.__repr__())
                table.drink_orders.append(current_drink)
            else:
                not_in_the_menu.append(drink_name)

        result = ordered_drinks + not_in_the_menu

        return "\n".join(result)

    def leave_table(self, table_number: int):
        table = self.__find_table(table_number)
        bill = table.get_bill()
        table.clear()
        self.total_income += bill
        result = [f"Table: {table_number}", f"Bill: {bill:.2f}"]

        return '\n'.join(result)

    def get_free_tables_info(self):
        info = [t.free_table_info() for t in self.tables_repository]
        return '\n'.join(info)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

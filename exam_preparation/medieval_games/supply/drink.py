from Python_OOP.exam_preparation.medieval_games.supply.supply import Supply


class Drink(Supply):
    def __init__(self, name: str, energy: int = 15):
        super().__init__(name, energy)

    def details(self):
        return f"Drink: {self.name}, {self.energy}"

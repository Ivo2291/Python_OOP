from Python_OOP.exam_preparation.astronauts.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    BREATHE_UNITS = 15

    def __init__(self, name: str, oxygen: int = 90):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= self.BREATHE_UNITS

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

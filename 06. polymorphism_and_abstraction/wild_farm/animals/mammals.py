from wild_farm.animals.animal import Mammal


class Mouse(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    @property
    def weight_gained(self):
        return 0.1

    @property
    def allowed_foods(self):
        return ["Vegetable", "Fruit"]


class Dog(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    @property
    def weight_gained(self):
        return 0.4

    @property
    def allowed_foods(self):
        return ["Meat"]


class Cat(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    @property
    def weight_gained(self):
        return 0.3

    @property
    def allowed_foods(self):
        return ["Vegetable", "Meat"]


class Tiger(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    @property
    def weight_gained(self):
        return 1

    @property
    def allowed_foods(self):
        return ["Meat"]

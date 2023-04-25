from wild_farm.animals.animal import Bird


class Owl(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    @property
    def weight_gained(self):
        return 0.25

    @property
    def allowed_foods(self):
        return ["Meat"]


class Hen(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    @property
    def weight_gained(self):
        return 0.35

    @property
    def allowed_foods(self):
        return ["Meat", "Vegetable", "Seed", "Fruit"]

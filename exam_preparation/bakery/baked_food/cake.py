from Python_OOP.exam_preparation.bakery.baked_food.baked_food import BakedFood


class Cake(BakedFood):
    def __init__(self, name: str, price: float):
        super().__init__(name, 245, price)

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"
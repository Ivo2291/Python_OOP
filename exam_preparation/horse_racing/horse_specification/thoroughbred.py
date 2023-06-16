from Python_OOP.exam_preparation.horse_racing.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140
    SPEED_INCREMENT = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        if self.speed + self.SPEED_INCREMENT <= self.MAX_SPEED:
            self.speed += self.SPEED_INCREMENT
        else:
            self.speed = self.MAX_SPEED

from Python_OOP.exam_preparation.horse_racing.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    SPEED_INCREMENT = 2

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        if self.speed + self.SPEED_INCREMENT <= self.MAX_SPEED:
            self.speed += self.SPEED_INCREMENT
        else:
            self.speed = self.MAX_SPEED

from collections import deque

from Python_OOP.exam_preparation.christmas_races.car.muscle_car import MuscleCar
from Python_OOP.exam_preparation.christmas_races.car.sports_car import SportsCar
from Python_OOP.exam_preparation.christmas_races.driver import Driver
from Python_OOP.exam_preparation.christmas_races.race import Race


class Controller:
    VALID_CAR_TYPES = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar
    }

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def _check_if_driver_exists(self, driver_name: str):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver
        else:
            raise Exception(f"Driver {driver_name} could not be found!")

    def _check_if_car_type_exists(self, car_type: str):
        for i in range(len(self.cars)-1, -1, -1):
            if type(self.cars[i]).__name__ == car_type:
                if not self.cars[i].is_taken:
                    return self.cars[i]
        else:
            raise Exception(f"Car {car_type} could not be found!")

    def _check_if_race_exists(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race

        else:
            raise Exception(f"Race {race_name} could not be found!")

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type in self.VALID_CAR_TYPES:
            for car in self.cars:
                if car.model == model:
                    raise Exception(f"Car {model} is already created!")

            new_car = self.VALID_CAR_TYPES[car_type](model, speed_limit)
            self.cars.append(new_car)

            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)

        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)

        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self._check_if_driver_exists(driver_name)
        car = self._check_if_car_type_exists(car_type)

        if driver.car:
            old_car = driver.car
            old_model = driver.car.model
            driver.car = car
            old_car.is_taken = False
            car.is_taken = True

            return f"Driver {driver_name} changed his car from {old_model} to {car.model}."

        driver.car = car
        car.is_taken = True

        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self._check_if_race_exists(race_name)
        driver = self._check_if_driver_exists(driver_name)

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        for d in race.drivers:
            if d.name == driver_name:
                raise Exception(f"Driver {driver_name} is already added in {race_name} race.")

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self._check_if_race_exists(race_name)
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        winners = deque(driver for driver in sorted(race.drivers, key=lambda driver: -driver.car.speed_limit))

        result = []

        for i in range(3):
            d = winners.popleft()
            d.number_of_wins += 1
            result.append(f"Driver {d.name} wins the {race_name}"
                          f" race with a speed of {d.car.speed_limit}.")

        return '\n'.join(result)

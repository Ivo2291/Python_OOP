from Python_OOP.exam_preparation.astronauts.astronaut.astronaut_repository import AstronautRepository
from Python_OOP.exam_preparation.astronauts.astronaut.biologist import Biologist
from Python_OOP.exam_preparation.astronauts.astronaut.geodesist import Geodesist
from Python_OOP.exam_preparation.astronauts.astronaut.meteorologist import Meteorologist
from Python_OOP.exam_preparation.astronauts.planet.planet import Planet
from Python_OOP.exam_preparation.astronauts.planet.planet_repository import PlanetRepository


class SpaceStation:
    VALID_TYPES = {
        "Biologist": Biologist,
        "Geodesist": Geodesist,
        "Meteorologist": Meteorologist
    }
    MISSION_IS_COMPLETED = False
    __failed_missions = 0
    __successful_missions = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in self.VALID_TYPES:
            raise Exception("Astronaut type is not valid!")

        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut:
            return f"{name} is already added."

        astronaut = self.VALID_TYPES[astronaut_type](name)
        self.astronaut_repository.add(astronaut)

        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        planet = self.planet_repository.find_by_name(name)
        if planet:
            return f"{name} is already added."

        new_planet = Planet(name)
        new_planet.items.extend(items.split(', '))
        self.planet_repository.add(new_planet)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut:
            self.astronaut_repository.astronauts.remove(astronaut)
            return f"Astronaut {name} was retired!"

        raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")

        astronauts = sorted(self.astronaut_repository.astronauts, key=lambda a: -a.oxygen)
        top_five = [a for a in astronauts if a.oxygen > 30][:5]
        number_of_explorers = 0

        if not top_five:
            raise Exception("You need at least one astronaut to explore the planet!")

        while True:
            if not top_five:
                break

            if not planet.items:
                self.MISSION_IS_COMPLETED = True
                break

            current_astronaut = top_five.pop(0)
            number_of_explorers += 1

            while planet.items:
                if current_astronaut.oxygen <= 0:
                    break
                current_astronaut.backpack.append(planet.items.pop())
                current_astronaut.breathe()

        if self.MISSION_IS_COMPLETED:
            self.__successful_missions += 1
            return f"Planet: {planet_name} was explored. {number_of_explorers}" \
                   f" astronauts participated in collecting items."
        else:
            self.__failed_missions += 1
            return "Mission is not completed."

    def report(self):
        result = [
            f"{self.__successful_missions} successful missions!",
            f"{self.__failed_missions} missions were not completed!",
            f"Astronauts' info:"
        ]

        for astronaut in self.astronaut_repository.astronauts:
            result.append(f"Name: {astronaut.name}")
            result.append(f"Oxygen: {astronaut.oxygen}")
            result.append(f"Backpack items:"
                          f" {', '.join([', '.join(astronaut.backpack) if astronaut.backpack else 'none'])}")

        return '\n'.join(result)

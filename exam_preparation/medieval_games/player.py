from medieval_games.supply.supply import Supply


class Player:
    players_list = []

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name not valid!")
        if value in self.players_list:
            raise Exception(f"Name {value} is already used!")

        self.players_list.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")

        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < 0 or value > 100:
            raise ValueError("Stamina not valid!")

        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.__stamina < 100

    def _player_sustain(self, supply: Supply):
        if self.stamina + supply.energy > 100:
            self.stamina = 100
        else:
            self.stamina += supply.energy

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"

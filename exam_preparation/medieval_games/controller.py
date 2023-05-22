class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def __check_if_player_exists(self, player_name):
        for p in self.players:
            if p.name == player_name:
                return p

    def __take_supply(self, supply_type):
        for i in range(len(self.supplies) - 1, 0, -1):
            if type(self.supplies[i]).__name__ == supply_type:
                return self.supplies.pop(i)
        if supply_type == "Food":
            raise Exception("There are no food supplies left!")
        if supply_type == "Drink":
            raise Exception("There are no drink supplies left!")

    @staticmethod
    def check_if_player_can_duel(*players):
        result = []
        for player in players:
            if player.stamina == 0:
                result.append(f"Player {player.name} does not have enough stamina.")
        if result:
            return '\n'.join(result)

    @staticmethod
    def __attack(first_player, second_player):
        second_player.stamina -= (first_player.stamina / 2)
        if first_player.stamina - (second_player.stamina / 2) < 0:
            first_player.stamina = 0
        else:
            first_player.stamina -= (second_player.stamina / 2)
        if first_player.stamina < second_player.stamina:
            return f"Winner: {second_player.name}"
        if second_player.stamina < first_player.stamina:
            return f"Winner: {first_player.name}"

    def add_player(self, *players):
        added_players = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player.name)

        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supplies):
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__check_if_player_exists(player_name)
        if player.stamina == 100:
            return f"{player_name} have enough stamina."

        supply = self.__take_supply(sustenance_type)

        if supply:
            player._player_sustain(supply)
            return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__check_if_player_exists(first_player_name)
        second_player = self.__check_if_player_exists(second_player_name)

        result = self.check_if_player_can_duel(first_player, second_player)

        if result:
            return result

        if first_player.stamina < second_player.stamina:
            return self.__attack(first_player, second_player)

        if second_player.stamina < first_player.stamina:
            return self.__attack(second_player, first_player)

    def next_day(self):
        for player in self.players:
            if player.stamina - (player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= (player.age * 2)

        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []

        for player in self.players:
            result.append(player.__str__())

        for supply in self.supplies:
            result.append(supply.details())

        return '\n'.join(result)

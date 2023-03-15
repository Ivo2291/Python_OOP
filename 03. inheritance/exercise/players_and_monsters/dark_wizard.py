from players_and_monsters.wizard import Wizard


class DarkWizard(Wizard):
    def __init__(self, name: str, level: int):
        super().__init__(name, level)

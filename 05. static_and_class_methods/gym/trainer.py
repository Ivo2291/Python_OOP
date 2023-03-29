class Trainer:
    ID = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Trainer.get_next_id()

        Trainer.ID += 1

    @staticmethod
    def get_next_id():
        return Trainer.ID

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

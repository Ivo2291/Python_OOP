from animal import Animal
from caretaker import Caretaker
from cheetah import Cheetah
from keeper import Keeper
from lion import Lion
from tiger import Tiger
from vet import Vet
from worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: float):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price

            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif self.__budget < price:
            return "Not enough budget"

        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)

            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            current_worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(current_worker)

        return f"{worker_name} fired successfully"

    def pay_workers(self):
        total_sum = sum([w.salary for w in self.workers])

        if total_sum <= self.__budget:
            self.__budget -= total_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_sum = sum([a.MONEY_FOR_CARE for a in self.animals])

        if total_sum <= self.__budget:
            self.__budget -= total_sum
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [repr(l) for l in self.animals if isinstance(l, Lion)]
        tigers = [repr(t) for t in self.animals if isinstance(t, Tiger)]
        cheetahs = [repr(ch) for ch in self.animals if isinstance(ch, Cheetah)]

        output = f"You have {len(self.animals)} animals\n"
        output += f"----- {len(lions)} Lions:\n" + '\n'.join(lions) + '\n'
        output += f"----- {len(tigers)} Tigers:\n" + '\n'.join(tigers) + '\n'
        output += f"----- {len(cheetahs)} Cheetahs:\n" + '\n'.join(cheetahs)

        return output

    def workers_status(self):
        keepers = [repr(k) for k in self.workers if isinstance(k, Keeper)]
        caretakers = [repr(c) for c in self.workers if isinstance(c, Caretaker)]
        vets = [repr(v) for v in self.workers if isinstance(v, Vet)]

        output = f"You have {len(self.workers)} workers\n"
        output += f"----- {len(keepers)} Keepers:\n" + '\n'.join(keepers) + '\n'
        output += f"----- {len(caretakers)} Caretakers:\n" + '\n'.join(caretakers) + '\n'
        output += f"----- {len(vets)} Vets:\n" + '\n'.join(vets)

        return output

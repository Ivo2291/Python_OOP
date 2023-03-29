from gym.customer import Customer
from gym.equipment import Equipment
from gym.exercise_plan import ExercisePlan
from gym.subscription import Subscription
from gym.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        self.__add_elements(self.customers, customer)

    def add_trainer(self, trainer: Trainer):
        self.__add_elements(self.trainers, trainer)

    def add_equipment(self, equipment: Equipment):
        self.__add_elements(self.equipment, equipment)

    def add_plan(self, plan: ExercisePlan):
        self.__add_elements(self.plans, plan)

    def add_subscription(self, subscription: Subscription):
        self.__add_elements(self.subscriptions, subscription)

    def subscription_info(self, subscription_id: int):
        subscription = [s for s in self.subscriptions if s.id == subscription_id][0]
        customer = [c for c in self.customers if c.id == subscription.customer_id][0]
        trainer = [t for t in self.trainers if t.id == subscription.trainer_id][0]
        plan = [p for p in self.plans if p.id == subscription.exercise_id][0]
        equipment = [e for e in self.equipment if e.id == plan.equipment_id][0]

        return f"{subscription}\n" \
               f"{customer}\n" \
               f"{trainer}\n" \
               f"{equipment}\n" \
               f"{plan}"

    @staticmethod
    def __add_elements(collection: list, obj):
        if obj not in collection:
            collection.append(obj)
        return

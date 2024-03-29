from customer import Customer
from dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    @staticmethod
    def __finder(collection, some_id):
        try:
            obj = next(filter(lambda x: x.id == some_id, collection))
        except StopIteration:
            return

        return obj

    def add_customer(self, customer: Customer):
        if MovieWorld.CUSTOMER_CAPACITY > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if MovieWorld.DVD_CAPACITY > len(self.dvds):
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = self.__finder(self.customers, customer_id)
        dvd = self.__finder(self.dvds, dvd_id)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True

        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.__finder(self.customers, customer_id)
        dvd = self.__finder(self.dvds, dvd_id)

        if customer and dvd:

            if dvd in customer.rented_dvds:
                customer.rented_dvds.remove(dvd)
                dvd.is_rented = False

                return f"{customer.name} has successfully returned {dvd.name}"

            return f"{customer.name} does not have that DVD"

    def __repr__(self):
        return "\n".join([repr(x) for x in self.customers]) + "\n" + "\n".join([repr(x) for x in self.dvds])

class Customer:
    ID = 1

    def __init__(self, name: str, address: str, email: str):
        self.email = email
        self.address = address
        self.name = name
        self.id = Customer.get_next_id()

        Customer.ID += 1

    @staticmethod
    def get_next_id():
        return Customer.ID

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

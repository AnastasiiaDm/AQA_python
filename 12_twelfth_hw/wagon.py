class Wagon:
    def __init__(self, number):
        self.number = number
        self.passengers = []

    def __len__(self):
        print(self.passengers)
        return len(self.passengers)

    def add_passenger(self, passenger):
        if len(self.passengers) >= 10:
            raise ValueError("Wagon is full")
        self.passengers.append(passenger)

    def __repr__(self):
        return f"[{self.number}]"
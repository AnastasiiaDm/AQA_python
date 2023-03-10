class Train:
    def __init__(self):
        self.wagons = []

    def __len__(self):
        print(self.wagons[1::])
        return len(self.wagons) - 1

    # def add_wagon(self, wagon: str):
    #     self.wagons.append(wagon)

    def __add__(self, wagon: str):
        self.wagons.append(wagon)
        return self

    def __str__(self):
        wagon_reprs = "-".join(repr(wagon) for wagon in self.wagons[::1])
        return f"<={wagon_reprs}"

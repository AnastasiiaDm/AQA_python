from abc import ABC


class Animals(ABC):
    def __init__(self, animal: str):
        self.animal = animal

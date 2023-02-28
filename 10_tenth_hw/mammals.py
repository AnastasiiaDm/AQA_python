"""
Describe mammals using principles from the lesson. You should implement different fields and methods.
For example:

Animals -> mammals -> flying mammals-> Bird -> Eagle

Minimum 3 chains should be implemented
Classes should be in different modules. You should have at least 5 different classes.
"""
from abc import abstractmethod
from animals import Animals


class Mammals(Animals):
    def __init__(self, animal: str):
        super().__init__(animal)

    @abstractmethod
    def eat(self): ...

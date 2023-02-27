from predators import Predators
from abc import abstractmethod


class Raccoons(Predators):
    def genus(self):
        return f'Raccoon'

    def eat(self):
        return f'omnivores'

    @abstractmethod
    def continent(self): ...

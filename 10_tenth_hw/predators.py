from mammals import Mammals
from abc import abstractmethod


# хищники
class Predators(Mammals):
    def eat(self):
        return f'carnivores, omnivores'

    @abstractmethod
    def genus(self): ...

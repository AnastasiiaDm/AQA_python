from abc import abstractmethod
from mammals import Mammals


class Cetaceans(Mammals):
    def eat(self):
        return f'carnivores'

    @abstractmethod
    def genus(self): ...

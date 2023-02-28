from abc import abstractmethod
from cetaceans import Cetaceans


class Wales(Cetaceans):
    def genus(self):
        return f'Wale'

    def eat(self):
        return f'carnivores'

    @abstractmethod
    def continent(self): ...

from artiodactyls import Artiodactyls
from abc import abstractmethod


class Pigs(Artiodactyls):
    def genus(self):
        return f'Pig'

    def eat(self):
        return f'omnivores'

    @abstractmethod
    def continent(self): ...

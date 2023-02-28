from artiodactyls import Artiodactyls
from abc import abstractmethod


# оленьи
class Reindeer(Artiodactyls):
    def genus(self):
        return f'Reindeer'

    def eat(self):
        return f'herbivores'

    @abstractmethod
    def continent(self): ...

from mammals import Mammals
from abc import abstractmethod


# парнокопытные
class Artiodactyls(Mammals):

    def eat(self):
        return f'herbivores, omnivores'

    @abstractmethod
    def genus(self): ...

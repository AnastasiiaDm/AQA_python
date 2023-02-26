"""
Describe mammals using principles from the lesson. You should implement different fields and methods.
For example:

Animals -> mammals -> flying mammals-> Bird -> Eagle

Minimum 3 chains should be implemented
Classes should be in different modules. You should have at least 5 different classes.
"""
from abc import ABC, abstractmethod


class Animals(ABC):

    def __init__(self, animal: str):
        self.animal = animal


class Mammals(Animals):
    def __init__(self, animal: str):
        super().__init__(animal)

    @abstractmethod
    def eat(self):
        pass


# парнокопытные
class Artiodactyls(Mammals):

    def eat(self):
        return f'herbivores, omnivores'

    @abstractmethod
    def genus(self):
        pass


# оленьи
class Reindeer(Artiodactyls):
    def genus(self):
        return f'Reindeer'

    def eat(self):
        return f'herbivores'

    @abstractmethod
    def continent(self):
        pass


class Doe(Reindeer):
    def continent(self):
        return f'Europe, Asia'


class Pigs(Artiodactyls):
    def genus(self):
        return f'Pig'

    def eat(self):
        return f'omnivores'

    @abstractmethod
    def continent(self):
        pass


class Boars(Pigs):
    def continent(self):
        return f'Europe, Asia, USA, India'


# хищники
class Predators(Mammals):
    def eat(self):
        return f'carnivores, omnivores'

    @abstractmethod
    def genus(self):
        pass


class Raccoons(Predators):
    def genus(self):
        return f'Raccoon'

    def eat(self):
        return f'omnivores'

    @abstractmethod
    def continent(self):
        pass


class TexasRaccoon(Raccoons):
    def continent(self):
        return f'Texas, Mexico'


# китообразные
class Cetaceans(Mammals):
    def eat(self):
        return f'carnivores'

    @abstractmethod
    def genus(self):
        pass


class Wales(Cetaceans):
    def genus(self):
        return f'Wale'

    def eat(self):
        return f'carnivores'

    @abstractmethod
    def continent(self):
        pass


class AntarcticBlueWhale(Wales):
    def continent(self):
        return f'Atlantic Ocean '


if __name__ == '__main__':
    cate = Cetaceans
    artiodactyls = Artiodactyls
    print(cate.eat('whale'))
    print(artiodactyls.eat('goal'))
    doe = Doe
    print(doe.eat('Doe'))
    print(doe.continent('Doe'))

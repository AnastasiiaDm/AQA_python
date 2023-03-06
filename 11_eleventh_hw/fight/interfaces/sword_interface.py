from abc import ABC, abstractmethod


# Inheritance
class ISword(ABC):

    # Abstraction
    @abstractmethod
    # hiding
    def _goal(self): ...

    # Abstraction
    @abstractmethod
    # hiding
    def _damage(self, damage: int): ...

    # Abstraction
    @abstractmethod
    # hiding
    def _combat_readiness(self): ...

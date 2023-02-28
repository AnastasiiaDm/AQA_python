from abc import ABC, abstractmethod


# Inheritance
class IWeapon(ABC):

    # Abstraction
    @abstractmethod
    # hiding
    def _get(self): ...

    # Abstraction
    @abstractmethod
    # hiding
    def _hit(self): ...

    # Abstraction
    @abstractmethod
    # hiding
    def _hide(self): ...

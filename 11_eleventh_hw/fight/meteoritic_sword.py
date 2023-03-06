from interfaces.weapon_interface import IWeapon
from interfaces.sword_interface import ISword


# Inheritance
# Abstraction
class MeteoriticSword(IWeapon, ISword):
    def __init__(self):
        # hiding
        self.__is_hidden = True
        self.__is_got = False
        self.__combat_readiness = False
        self.__hit = False
        self.__goal = False
        self.__damage = 0
        self.__enemy_hp = 30

    # Polymorphism
    def _get(self):
        self._hide()
        print('take off the sword')
        self.__is_got = True

    # Polymorphism
    def _hit(self):
        self._goal()
        print('I hit an enemy')
        self.__hit = True

    # Polymorphism
    def _hide(self):
        print("The weapon is hidden")
        self.__is_hidden = True

    # Polymorphism
    def _goal(self):
        self._combat_readiness()
        print('Enemy is chosen')
        self.__goal = True

    # Polymorphism
    def _damage(self, damage: int):
        self._hit()
        print(f'Enemy is injured by {damage} HP')
        self.__damage = damage

    # Polymorphism
    def _combat_readiness(self):
        self._get()
        print('the sword is ready for the fight')
        self.__combat_readiness = True

    # Encapsulation
    def fight(self):
        self._damage(31)
        if self.__damage < self.__enemy_hp:
            print("enemy is still alive")
        else:
            print("Enemy RIP")
            self._hide()

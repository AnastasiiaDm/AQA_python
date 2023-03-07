"""
Describe any object of your choice in the class. I want the object to be printed to the console in the following format:
class_name: {

key: value

}
"""


class Magic:
    def __init__(self, mana: int):
        self.mana = mana

    def __str__(self):
        return f'{self.__class__.__name__}: {self.__dict__}'


if __name__ == '__main__':
    magic = Magic(10)
    print(magic)

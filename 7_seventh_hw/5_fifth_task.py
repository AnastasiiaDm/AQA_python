"""
Implement your own all function
"""
from typing import Callable


def find_all(data: list) -> bool:
    for element in data:
        if not element:
            return False
    return True


def my_all(callback: Callable, data: list):
    return callback(data)


if __name__ == '__main__':
    my_all(find_all, [1, 2, 3, 0.5, 2.1, 'a'])

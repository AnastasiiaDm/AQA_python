"""
Implement your own implementation of the function map
"""
from typing import Callable


def multiply_by_2(data: list) -> list:
    """
    :param data: integers, floats, strings
    :return: mapped list
    """
    new_list = []
    for element in data:
        new_list.append(element * 2)
    return new_list


def my_map(callback: Callable, data: list):
    """
    :param callback: data map
    :param data: integers, floats, strings
    :return: list of mapped elements
    """
    return callback(data)


if __name__ == '__main__':
    my_map(multiply_by_2, [1, 2, 3, 0.5, 2.1, 'a'])

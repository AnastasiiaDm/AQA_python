"""
Implement your own implementation of function max and min
(* additional argument amount of result, if you pass 2, function should return 2 max values from the list)
"""
from typing import Callable


def find_max(data: list) -> tuple:
    max_element = data[0]
    second_max_element = data[0]
    for element in data:
        if element > max_element:
            max_element = element
        elif element < max_element:
            second_max_element = element
    return max_element, second_max_element


def find_min(data: list) -> int or float:
    max_element = data[0]
    for element in data:
        if element < max_element:
            max_element = element
    return max_element


def my_max_min(callback: Callable, data: list):
    return callback(data)


if __name__ == '__main__':
    my_max_min(find_max, [1, 2, 3, 0.5, 2.1])
    my_max_min(find_min, [1, 2, 3, 0.5, 2.1])

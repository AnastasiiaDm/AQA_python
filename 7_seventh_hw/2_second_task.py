"""
Implement your realization of the function filter
must have the following signature def function_name(callback, sequence). Add annotations yourself. Functions must be
able to work with integers, floats, and strings as elements of sequences.
"""
from typing import Callable


def multiple_type_sort(data: str) -> tuple:
    try:
        ele = int(data)
        return False, ele
    except ValueError:
        return True, data


def my_filter(callback: Callable, data: list):
    """
    :param callback: sort data
    :param data: integers, floats, strings
    :return: tuple with 2 elements: "(True, "[sorted data]")"
    """
    data.sort(key=multiple_type_sort)
    return callback(str(data))


if __name__ == '__main__':
    my_filter(multiple_type_sort, [1, 2, 3, 0.5, 2.1, "b", "a"])

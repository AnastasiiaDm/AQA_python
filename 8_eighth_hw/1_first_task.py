"""
Create a decorator that prints to the console the name of the function that was called. The function should work as
intended. For example, create a pair of functions for the arithmetic operations of summation and multiplication.
When calling these functions, the result of the operation must be returned and the name of the function that was called
must be displayed in the console with the result. Small hint (__name__)
"""


def func_name_decorator(symbol, quantity):
    def func_call(func):
        def inner(number_1, number_2):
            start_symbol, end_symbol = symbol * quantity, symbol * quantity
            return f'{start_symbol}{func.__name__}{end_symbol}\n{func(number_1, number_2)}'

        return inner

    return func_call


@func_name_decorator('_', 2)
def summation(number_1, number_2):
    return number_1 + number_2


@func_name_decorator('_', 2)
def multiplication(number_1, number_2):
    return number_1 * number_2


if __name__ == '__main__':
    print(summation(3, 2))
    print(multiplication(3, 2))

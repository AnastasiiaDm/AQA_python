"""
Create a function that can return the squares of even elements for the range 0 to 1000000000 inclusive. The solution
should work and not freeze your computer.
"""
import sys


def even_square_generator():
    counter = 0
    while counter % 2 == 0:
        yield counter ** 2
        counter += 2
        if counter > 1000000000:
            break


if __name__ == '__main__':
    even_squares = even_square_generator()
    print(f'generator size: {sys.getsizeof(even_squares)}')
    for even_square in even_squares:
        print(even_square)

"""
2. Write a function square that takes 1 argument, the side of the square, and returns 3 values (using a tuple):
the perimeter of the square, the area of square, and the diagonal of the square.
"""
import math

if __name__ == '__main__':
    def square_parameters(square_side: int) -> tuple:
        square_perimeter = square_side * 4
        square_area = square_side ** 2
        square_diagonal = math.sqrt(square_area * 2)
        result = (square_perimeter, square_area, square_diagonal)
        return result

"""
3. Write a function is_prime that takes 1 argument - a number from 2 to 1000, and returns True if it is a prime number,
and False otherwise.
"""
if __name__ == '__main__':
    def is_prime_number(number: int) -> bool:
        if number in range(2, 1001):
            for num in range(2, int(number / 2) + 1):
                if (number % num) == 0:
                    return False
            else:
                return True

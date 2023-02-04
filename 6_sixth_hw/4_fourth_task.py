"""
4. You have a file of unknown length. Write a function that will remove all numbers from each line of the file.
"""
import re


def remove_numbers_from_file(file_name):
    with open(file_name, "r+") as file:
        text_file = file.read()

    with open(file_name, "w") as file:
        file.write(re.sub(r'\d+', "", text_file))


if __name__ == '__main__':
    remove_numbers_from_file("test_1.py")

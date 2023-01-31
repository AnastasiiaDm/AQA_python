"""
4. You have a file of unknown length. Write a function that will remove all numbers from each line of the file.
"""
import re

if __name__ == '__main__':
    with open("test_1.py", "r") as file:
        text_file = file.read()


    def remove_numbers(text):
        no_num_text = re.sub(r'\d+', "", text)
        return no_num_text


    with open("test_1.py", "w") as file:
        file.write(remove_numbers(text_file))

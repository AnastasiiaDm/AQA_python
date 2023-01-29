"""
Create a list of tuples with a length of 100 elements where each tuple consists of 3 elements:

a. element is an integer that will be the left operand of the expression

b. element is an integer that will be the right operand of the expression

c. element is an integer from 1 to 3 where:

identifies the addition operation
identifies the subtraction operation
identifies the multiplication operation

d. You can put data into a text file with the text form or use the pickle module in binary form. If placed as text then
each line should contain only elements of one tuple separated by spaces (eg "100 2 3"). The file must be created by a
script in a pre-created \test\data directory tree. The directory tree must be created by the script. Push only the code
to the repository (not directories or file).
"""
import os
import pickle
import random

my_list = []

if __name__ == '__main__':
    # os.mkdir("files")
    os.chdir("./files")
    for _ in range(1, 101):
        my_list.append((random.randrange(1, 100), random.randrange(1, 4), random.randrange(1, 100)))

    byte_numbers = pickle.dumps(my_list)
    with open('byte_file', 'w+b') as file:
        file.write(byte_numbers)

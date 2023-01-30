"""
2. Using the created file in task 1, read the file and perform mathematical operations on each element. Output the
result of the operation to the console. You cannot use imports to import from the first task module.
"""
import os
import pickle
import sys

if __name__ == '__main__':
    os.chdir("./test/data")
    with open('byte_file', 'rb') as file:
        result_in_bytes = file.read()

    result = pickle.loads(result_in_bytes)

    new_list = []
    for integers in result:
        if integers[2] == 1:
            new_list.append(integers[0] + integers[1])
        if integers[2] == 2:
            new_list.append(integers[0] - integers[1])
        if integers[2] == 3:
            new_list.append(integers[0] * integers[1])

    math_result_in_str = str(new_list)
    print(sys.stderr.write(math_result_in_str))

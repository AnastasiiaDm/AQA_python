"""
2. Using the created file in task 1, read the file and perform mathematical operations on each element. Output the
result of the operation to the console. You cannot use imports to import from the first task module.
"""
import os
import pickle
import sys

if __name__ == '__main__':
    os.chdir("files")
    with open('byte_file', 'rb') as file:
        result_in_bytes = file.read()

    result = pickle.loads(result_in_bytes)

    new_list = []
    for integers in result:
        addition = integers[0] + integers[1] + integers[2]
        subtraction = integers[0] - integers[1] - integers[2]
        multiplication = integers[0] * integers[1] * integers[2]
        math_result = (addition, subtraction, multiplication)
        new_list.append(math_result)
    math_result_in_str = str(new_list)
    print(sys.stderr.write(math_result_in_str))

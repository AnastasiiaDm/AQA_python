"""
3. You have the file text.txt(attached). Please count how many times each letter appears in this file.
"""
import os
import re

if __name__ == '__main__':
    os.chdir("./files")
    with open('text.txt', "r") as file:
        file_str = file.read()
    words = re.findall(r"[a-zA-Z]", file_str)
    words.sort()

    result_dict = {}
    for letter in words:
        result_dict[letter] = words.count(letter)
    print(result_dict)

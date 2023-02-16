"""
you have a text break the text(attached file) into sentences. As a result, you should get a list of sentences.
"""
import re

if __name__ == '__main__':
    with open('text.txt', 'r') as file:
        text = file.read()
    print(re.findall(r"\b[^.]+[.]+", text))

# right solution:
if __name__ == '__main__':
    with open('text.txt', 'r') as file:
        text = file.read()
    print(re.split(r'\.\s|\.(?=A commission)', text))

"""
Implement your own print function. It should work on all operating systems. You can't use build-in print function
"""
import sys


def stderr_print(text: str):
    sys.stderr.write(f'{str(text)}\n')


def stdout_print(text: str):
    sys.stdout.write(f'{str(text)}\n')


if __name__ == '__main__':
    stderr_print("stderr_print")
    stdout_print("stdout_print")

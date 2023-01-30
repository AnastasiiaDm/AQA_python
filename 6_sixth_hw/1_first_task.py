"""
1. Write an arithmetic function that takes 3 arguments: the first 2 are numbers, and the third is the operation to be
performed on them.
If the third argument is +, add them up; if -, then subtract; * - multiply; / - divide (first to second).
Otherwise, return the string Not known operation: {operation}.

Describe the function in the attached file in such a way that all checks in the __main__ task_1 block are performed
correctly.
DO NOT CALL THE FUNCTION YOURSELF I HAVE ALREADY DONE THIS IN "assert" STATEMENTS
"""
if __name__ == '__main__':
    def arithmetic_function(num_1: int, num_2: int, operation: str) -> int or str or float:
        if operation == "+":
            result = num_1 + num_2
            return result
        if operation == "-":
            result = num_1 - num_2
            return result
        if operation == "*":
            result = num_1 * num_2
            return result
        if operation == "/":
            result = num_1 / num_2
            return result
        else:
            return f"Not known operation: {operation}"

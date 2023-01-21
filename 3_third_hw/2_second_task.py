"""
You have the number 2 as a variable. Multiply it by 2 in two ways. Accordingly, you need to divide it in 2 different
ways by 2.
"""
number_two = 2

first_multiply = bin(number_two * 2)
print(f'first_multiply: {int(first_multiply, 2)}')

if number_two == 2:
    second_multiply = number_two * 2
    print(f'second_multiply: {second_multiply}')

first_divide = number_two
while number_two == 2:
    first_divide //= 2
    break
print(f'third_multiply: {first_divide}')

second_divide = [int(number) // 2 for number in str(number_two)]
print(f'fourth_multiply: {second_divide[0]}')

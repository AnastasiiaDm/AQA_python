"""
there is a string " name=Amanda=sssss&age=32&&salary=1500&currency=euro ". Convert this string to a dictionary
{name: Amanda, age: 32, salary: 1500, currency: quro}
"""

my_str = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "
# my_str_no_spaces = str(my_str.split("="))
# my_str_without_sss = my_str.replace("=sssss", "").replace("&", " ", 1).replace("&&", " ").replace("&", " ")
result = my_str.replace("=sssss&", " ").replace("&&", " ").replace("&", " ")
# print(my_str_without_sss)
my_dictionary = dict(some_variable.split("=") for some_variable in result.split())
print(result)
print(my_dictionary)

# print("Start of script".center(50, '-'))


# cookie = "name=John=John&age=23"
# pairs = cookie.split('&')
# print(pairs)
# for pair in pairs:
#     print(pair.split('=', maxsplit=1))
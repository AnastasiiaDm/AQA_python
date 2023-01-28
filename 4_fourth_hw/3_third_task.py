"""
there is a string " name=Amanda=sssss&age=32&&salary=1500&currency=euro ". Convert this string to a dictionary
{name: Amanda, age: 32, salary: 1500, currency: quro}
"""

my_str = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "

if __name__ == '__main__':
    result = my_str.replace("=sssss&", " ").replace("&&", " ").replace("&", " ")
    my_dictionary = dict(some_variable.split("=") for some_variable in result.split())

    print(my_dictionary)

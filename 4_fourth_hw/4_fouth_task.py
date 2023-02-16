"""
you have a list of variable names in camel case format ["FirstItem", "FriendsList", "MyTuple"] convert it to a list of
variable names for python in snake case format ["first_item", "friends_list", "my_tuple"]
"""
import re

variable_list = ["FirstItem", "FriendsList", "MyTuple"]
new_list = []

if __name__ == '__main__':
    variable_str = " ".join(variable_list)

    result = ''.join('_' + char.lower() if char.isupper() else char
                     for char in variable_str).split()
    for r in result:
        stripped = r.lstrip("_")
        new_list.append(stripped)
    print(new_list)

# anoter way of solution:
if __name__ == '__main__':
    pattern = re.compile(r'([A-Z][a-z]+)([A-Z][a-z]+)')
    matches = pattern.sub(r'\1_\2', ','.join(variable_list)).lower()
    result = matches.split(',')
    print(result)

# anoter way of solution2:
new_list2 = []
if __name__ == '__main__':
    for name in variable_list:
        some = re.sub(r"([A-Z][a-z]+)([A-Z][a-z]+)", r"\1_\2", name).lower()
        new_list2.append(some)
    print(new_list2)

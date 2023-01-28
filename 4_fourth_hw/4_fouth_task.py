"""
you have a list of variable names in camel case format ["FirstItem", "FriendsList", "MyTuple"] convert it to a list of
variable names for python in snake case format ["first_item", "friends_list", "my_tuple"]
"""

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

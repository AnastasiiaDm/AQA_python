"""
there is a list of friends ["John", "Marta", "James", "Amanda", "Marianna"]. print to the console the names of each on
a new line, right-aligned using the string method and formatting via f string. Also, above the names, in the first line,
 display the headings Names where the word names should be in the middle, and the rest of the space is filled with the
 symbol "*"
"""

friends_list = ["John", "Marta", "James", "Amanda", "Marianna"]

if __name__ == '__main__':
    print(f'Names'.center(20, "*"))
    for friends in range(0, len(friends_list)):
        print(f'{friends_list[friends] : >15}')

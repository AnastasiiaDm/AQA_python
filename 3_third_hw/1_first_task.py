"""
you have a list of elements [1, 2, 3, 4, 5, 6, 7, 8]. Loop through the list using the foreach loop. The element with an
odd index is put into a new list of tuples where the first element is the index and the second is the value.
[(index, value)]. accordingly, elements with an even index are placed in another list of tuples with the same format as
in the case with odd indices.
"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8]

odd_index_elements = []
even_index_elements = []

for index, element in enumerate(my_list):
    if index % 2 != 0:
        odd_index_elements.append((index, element))
    else:
        even_index_elements.append((index, element))
print(f'odd index elements: {odd_index_elements}')
print(f'even index elements: {even_index_elements}')

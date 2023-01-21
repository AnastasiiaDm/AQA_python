"""
you have a list of elements [1, 2, 3, 4, 5, 6, 7, 8]. Loop through the list using the foreach loop. The element with an
odd index is put into a new list of tuples where the first element is the index and the second is the value.
[(index, value)]. accordingly, elements with an even index are placed in another list of tuples with the same format as
in the case with odd indices.
"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8]

odd_index_elements = []
even_index_elements = []

odd_index = []
odd_elements = []

even_index = []
even_elements = []

for index in range(len(my_list)):
    if index % 2 != 0:
        odd_index.append(index)
        odd_elements.append(my_list[index])
        odd_index_elements = list(zip(odd_index, odd_elements))
    else:
        even_index.append(index)
        even_elements.append(my_list[index])
        even_index_elements = list(zip(even_index, even_elements))

print(f'odd index elements: {odd_index_elements}')
print(f'even index elements: {even_index_elements}')

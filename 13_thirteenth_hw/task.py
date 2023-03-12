"""
Create an iterator that accepts a sequence and can iterate over values in a given range.
CustomIterator(sequence, start_index, end_index)
"""


class CustomIterator:
    def __init__(self, sequence, start_index, end_index):
        self.__sequence = sequence
        self.__start_index = start_index
        self.__end_index = end_index
        self.__current_position = 0
        self.__iterated_list = self.__sequence[self.__start_index:self.__end_index]

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_position < len(self.__iterated_list):
            value = self.__iterated_list[self.__current_position]
            self.__current_position += 1
            return value
        else:
            raise StopIteration


if __name__ == '__main__':
    my_iter = CustomIterator([10, 20, 30, 40, 50], 1, 3)

    for value_ in my_iter:
        print(value_)

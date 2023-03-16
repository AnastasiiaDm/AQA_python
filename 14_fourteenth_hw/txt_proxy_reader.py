from reader import Reader
from writer import Writer
from txt_reader import TxtReader
from txt_writer import TxtWriter


class TxtProxy(Reader, Writer):
    def __init__(self, txt_reader: TxtReader, txt_writer: TxtWriter):
        self.__result = ''
        self.__is_actual = False
        self.__reader = txt_reader
        self.__writer = txt_writer
        # self.__new_data = ''

    def read(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__reader.read()
            self.__is_actual = True
            return self.__result

    def write(self, new_data):

        if self.__result != new_data:
            self.__writer.write(new_data)
            self.__is_actual = False

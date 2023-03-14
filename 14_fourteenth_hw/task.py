"""
Get code from the lesson.

Add writer to a proxy pattern.
When you call write to file status of file should change and read should call from TxTReader.
"""
from txt_reader import TxtReader
from txt_writer import TxtWriter
from txt_proxy_reader import TxtProxy

if __name__ == '__main__':
    read_file = TxtReader('my_file.txt')
    add_text = TxtWriter('my_file.txt')
    proxy = TxtProxy(read_file, add_text)
    print(proxy.read())
    print(proxy.write('\nololo'))
    print(proxy.read())

    print(proxy.write('\nololo'))

    print(proxy.read())

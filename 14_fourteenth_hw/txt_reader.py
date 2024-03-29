from reader import Reader


class TxtReader(Reader):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'r') as file:
            text = file.read()
        return text

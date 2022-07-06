from FileAndFolder.ReadFile.File import *


class TxtFile(file):
    data: str
    path: str

    def __init__(self, path: str) -> None:
        """
        :param path: str path to file
        :param path:
        """
        self.path: str = path
        self.read()

    def read(self) -> None:
        """
        read file
        :return:
        """
        try:
            with open(self.path, 'r') as f:
                self.data = f.read()
                f.close()
        except Exception as e:
            print(e)
            exit()

    def write(self, data: str) -> None:
        """
        write data to file
        :param data:
        :return:
        """
        try:
            with open(self.path, 'w') as f:
                f.write(data)
                f.close()
        except Exception as e:
            print(e)
            exit()

    def getData(self) -> str:
        """
        get data
        :return:
        """
        return self.data

    def __add__(self, data: str) -> None:
        """
        add two file
        :param other:
        :return:
        """
        self.data += data
        self.write(self.data)

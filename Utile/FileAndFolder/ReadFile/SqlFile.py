from Utile.FileAndFolder.ReadFile.File import *


class SqlFile(file):
    path: str
    data: str

    def __init__(self, path) -> None:
        super().__init__(path=path)

    def read(self) -> None:
        """
        read file
        :return:
        """
        try:
            print("Reading: " + self.getPath())
            with open(self.path, 'r', encoding="utf8") as file:
                self.data = file.read()
        except Exception as e:
            print(e)
            exit()

    def write(self, data: object) -> None:
        """
        write data
        :param data:
        :return:
        """
        pass

    def getData(self) -> str:
        """
        get data
        :return:
        """
        return self.data

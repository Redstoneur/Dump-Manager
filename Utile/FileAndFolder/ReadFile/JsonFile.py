from Utile.FileAndFolder.ReadFile.File import *
import json


######################################################################################################################
############################## Class JSON File #######################################################################
######################################################################################################################

class JsonFile(file):
    data: dict
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
                self.data = json.load(f)
                f.close()
        except Exception as e:
            print(e)
            exit()

    def write(self, data: dict) -> None:
        """
        write data to file
        :param data:
        :return:
        """
        try:
            with open(self.path, 'w') as f:
                json.dump(data, f)
                f.close()
        except Exception as e:
            print(e)
            exit()

    def getData(self) -> dict:
        """
        get data
        :return:
        """
        return self.data

    def get(self, key: str) -> object:
        """
        get data of key
        :param key:
        :return:
        """
        if key in self.data.keys():
            return self.data[key]
        else:
            return None

    def set(self, key: str, value: str) -> None:
        """
        set data of key
        :param key:
        :param value:
        :return:
        """
        self.data[key] = value
        self.write(self.data)

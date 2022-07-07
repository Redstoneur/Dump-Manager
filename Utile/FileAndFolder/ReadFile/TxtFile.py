from Utile.FileAndFolder.ReadFile.File import *


######################################################################################################################
############################## Class TXT File ########################################################################
######################################################################################################################

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

    def getPath(self) -> str:
        """
        get path
        :return:
        """
        return self.path

    def __add__(self, data: str) -> None:
        """
        add two file
        :param other:
        :return:
        """
        self.data += data
        self.write(self.data)


######################################################################################################################
############################## Special Functions #####################################################################
######################################################################################################################

def createTxtFile(path: str) -> bool:
    """
    create a txt file
    :param path: path to file
    :param content: content of the file
    :return: None
    """
    if path.split('.')[-1] == "txt":
        try:
            f = open(path, "w")
            f.write("")
            f.close()
        except Exception as e:
            print(e)
            print("Error: can't create file")
            return False
        else:
            print("File created")
            return True
    else:
        print("Not a txt file")
        return False

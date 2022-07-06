import os


class FoldersContained:
    path: str
    folders: list

    def __init__(self, path: str) -> None:
        """
        :param path: path to the folder containing files to read
        """
        self.path: str = path
        self.readFoldersContained()

    def readFoldersContained(self) -> None:
        """
        read all folders contained in the path
        :return:
        """
        try:
            self.folders = os.listdir(self.path)
        except Exception as e:
            print(e)
            exit()

    def getFolders(self) -> list:
        """
        :return: list of folders contained in the path
        """
        return self.folders

    def getPath(self) -> str:
        """
        :return: path to the folder containing files to read
        """
        return self.path

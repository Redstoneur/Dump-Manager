from abc import abstractmethod, ABC


class file(ABC):
    data: object
    path: str

    @abstractmethod
    def __init__(self, path: str) -> None:
        """
        :param path: str path to file
        """
        self.path = path
        pass

    @abstractmethod
    def read(self):
        """
        read file
        :return:
        """
        pass

    @abstractmethod
    def write(self, data: object):
        """
        write data to file
        :param data: object
        :return:
        """
        pass

    @abstractmethod
    def getData(self):
        """
        get data
        :return:
        """
        pass

    def getPath(self) -> str:
        """
        get path
        :return:
        """
        return self.path

    def getName(self) -> str:
        """
        get name
        :return:
        """
        return self.path.split('/')[-1]

    def getNameWithoutExtension(self) -> str:
        """
        get name without extension
        :return:
        """
        return self.getName().split('.')[0]

    def getExtension(self) -> str:
        """
        get extension
        :return:
        """
        return self.getName().split('.')[-1]

    def getNameWithoutExtensionAndPath(self) -> str:
        """
        get name without extension and path
        :return:
        """
        return self.getName().split('.')[0]

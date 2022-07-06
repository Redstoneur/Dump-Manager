from FileAndFolder.ReadFile.SqlFile import *
from Utile.Calendar import Date


class dumpSqlFile(SqlFile):
    path: str
    data: str
    dateOfDump: Date

    def __init__(self, path: str):
        """
        :param path: str, the path of the dump file
        """
        super().__init__(path)
        self.setDateOfDumpObject()

    def getNameDataBase(self) -> str:
        """
        get the name of the database
        :return: str, the name of the database
        """
        return '_'.join(self.getNameWithoutExtensionAndPath().split('_')[:-1])

    def setDateOfDumpObject(self) -> None:
        """
        set the date of the dump in a Date object
        :return: None
        """
        date = self.getNameWithoutExtensionAndPath().split('_')[-1].replace("(", "").replace(")", "").split('-')
        date.reverse()
        self.dateOfDump = Date(int(date[0]), int(date[1]), int(date[2]))

    def getDateOfDump(self) -> str:
        """
        get the date of the dump
        :return: str, the date of the dump
        """
        return str(self.dateOfDump.Day) + "-" + str(self.dateOfDump.Month) + "-" + str(self.dateOfDump.Year)

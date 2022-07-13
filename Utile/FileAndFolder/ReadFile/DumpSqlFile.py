from Utile.FileAndFolder.ReadFile.SqlFile import *
from Utile.Calendar import Date


######################################################################################################################
############################## Class Dump SQL File ###################################################################
######################################################################################################################

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
        return self.dateOfDump.getDayString() + "-" + self.dateOfDump.getMonthString() + "-" + self.dateOfDump.getYearString()


######################################################################################################################
############################## Special Functions #####################################################################
######################################################################################################################

def isDumpSqlFile(path: str) -> bool:
    """
    check if the file is a dump sql file
    :param path: str, the path of the file
    :return: bool, True if the file is a dump sql file, False if not
    """
    return path.split('.')[-1] == "sql"


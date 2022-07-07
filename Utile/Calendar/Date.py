import datetime as dt


######################################################################################################################
############################## Class Date ############################################################################
######################################################################################################################

class Date:
    Day: int = 0
    Month: int = 0
    Year: int = 0

    def __init__(self, day: int = Day, month: int = Month, year: int = Year) -> None:
        """
        Constructor of the class Date
        :param day: int
        :param month: int
        :param year: int
        """
        self.Day = day
        self.Month = month
        self.Year = year

    def setActualDate(self) -> None:
        """
        Set the actual date
        :return: None
        """
        now = dt.datetime.now()
        self.Day = now.day
        self.Month = now.month
        self.Year = now.year

    def __str__(self) -> str:
        """
        String representation of the class Date
        :return: str
        """
        day: str = "0" + str(self.Day) if self.Day < 10 else str(self.Day)
        month: str = "0" + str(self.Month) if self.Month < 10 else str(self.Month)
        year: str = str(self.Year)
        return day + "/" + month + "/" + year

    def __eq__(self, other) -> bool:
        """
        Compare two dates
        :param other: Date
        :return: bool
        """
        # if other is a Date
        if isinstance(other, Date):
            return self.Day == other.Day and self.Month == other.Month and self.Year == other.Year
        else:
            return False


######################################################################################################################
############################## Special Functions #####################################################################
######################################################################################################################

def getActualDate() -> Date:
    """
    Get the actual date
    :return: Date
    """
    date = Date()
    date.setActualDate()
    return date
import time as t


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
        now: t.struct_time = t.localtime()
        # day
        self.Day = now.tm_mday
        # month
        self.Month = now.tm_mon
        # year
        self.Year = now.tm_year

    def getDayString(self) -> str:
        """
        Get the day in string format
        :return: str
        """
        return "0" + str(self.Day) if self.Day < 10 else str(self.Day)

    def getMonthString(self) -> str:
        """
        Get the month in string format
        :return: str
        """
        return "0" + str(self.Month) if self.Month < 10 else str(self.Month)

    def getYearString(self) -> str:
        """
        Get the year in string format
        :return: str
        """
        return str(self.Year)

    def __str__(self) -> str:
        """
        String representation of the class Date
        :return: str
        """
        return self.getDayString() + "/" + self.getMonthString() + "/" + self.getYearString()

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

    def NumberOfDaysInMonth(self) -> int:
        """
        Calculate the number of days in the month
        :return: int
        """
        # if the month is February
        if self.Month == 2:
            # if the year is a leap year
            if self.Year % 4 == 0:
                return 29
            else:
                return 28
        # if the month is a month with 30 days
        elif self.Month in [4, 6, 9, 11]:
            return 30
        # if the month is a month with 31 days
        else:
            return 31

    def anterior(self, other) -> bool:
        """
        Compare two dates
        :param other: Date
        :return: bool
        """
        # if other is a Date
        if isinstance(other, Date):
            return self.Year < other.Year \
                   or (self.Year == other.Year and self.Month < other.Month) \
                   or (self.Year == other.Year and self.Month == other.Month and self.Day < other.Day)
        else:
            return False

    def posterior(self, other) -> bool:
        """
        Compare two dates
        :param other: Date
        :return: bool
        """
        # if other is a Date
        if isinstance(other, Date):
            return self.Year > other.Year \
                   or (self.Year == other.Year and self.Month > other.Month) \
                   or (self.Year == other.Year and self.Month == other.Month and self.Day > other.Day)
        else:
            return False

    def differenceInDays(self, other) -> int:
        """
        Calculate the difference between two dates in days
        :param other: Date
        :return: int
        """
        # if the other date is a Date
        if isinstance(other, Date):
            if self.__eq__(other):  # if is the same Date
                return 0
            elif self.posterior(other):  # if the other date is after the current date
                # calculate the difference
                return other.differenceInDays(self)
            else:
                # calculate the difference
                return self.NumberOfDaysInMonth() - self.Day + other.Day
        else:
            return 0


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

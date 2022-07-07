import datetime as dt
from Utile.Calendar.DateTime import *


######################################################################################################################
############################## Class WeekDay #########################################################################
######################################################################################################################

class WeekDay:
    dateTime: DateTime = DateTime()
    weekDay: int = None
    weekDayName: str = None

    def __init__(self, dateTime: DateTime = dateTime) -> None:
        """
        Constructor of the class WeekDay
        :param dateTime: DateTime
        """
        self.dateTime = dateTime
        self.setWeekDay()

    def setWeekDay(self) -> None:
        """
        Set the week day
        :return: None
        """
        weekDayNames: [str] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.weekDay = dt.datetime(day=self.dateTime.Date.Day,
                                   month=self.dateTime.Date.Month,
                                   year=self.dateTime.Date.Year).weekday()
        self.weekDayName = weekDayNames[self.weekDay]

    def setActualWeekDay(self) -> None:
        """
        Set the actual week day
        :return: None
        """
        self.dateTime.setActualDateTime()
        self.setWeekDay()

    def __str__(self) -> str:
        """
        String representation of the class WeekDay
        :return: str
        """
        return self.weekDayName + " " + str(self.dateTime)

    def __eq__(self, other) -> bool:
        """
        Compare two week days
        :param other: WeekDay
        :return: bool
        """
        # if other is a WeekDay
        if isinstance(other, WeekDay):
            return self.weekDay == other.weekDay
        else:
            return False


######################################################################################################################
############################## Special Functions #####################################################################
######################################################################################################################

def getActualWeekDay() -> WeekDay:
    """
    Get the actual week day
    :return: WeekDay
    """
    return WeekDay(getActualDateTime())

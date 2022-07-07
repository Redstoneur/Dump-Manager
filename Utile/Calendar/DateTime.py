from Utile.Calendar.Date import *
from Utile.Calendar.Time import *


######################################################################################################################
############################## Class DateTime ########################################################################
######################################################################################################################

class DateTime:
    Date: Date = Date()
    Time: Time = Time()

    def __init__(self, date: Date = Date, time: Time = Time) -> None:
        """
        Constructor of the class DateTime
        :param date: Date
        :param time: Time
        """
        self.Date = date
        self.Time = time

    def setActualDateTime(self) -> None:
        """
        Set the actual date and time
        :return: None
        """
        self.Date.setActualDate()
        self.Time.setActualTime()

    def __str__(self) -> str:
        """
        String representation of the class DateTime
        :return: str
        """
        return str(self.Date) + " " + str(self.Time)

    def __eq__(self, other) -> bool:
        """
        Compare two dates and times
        :param other: DateTime
        :return: bool
        """
        # if other is a DateTime
        if isinstance(other, DateTime):
            return self.Date == other.Date and self.Time == other.Time
        else:
            return False


######################################################################################################################
############################## Special Functions #####################################################################
######################################################################################################################

def getActualDateTime() -> DateTime:
    """
    Get the actual date and time
    :return: DateTime
    """
    return DateTime(getActualDate(), getactualTime())

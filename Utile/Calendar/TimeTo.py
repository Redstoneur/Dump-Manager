from Utile.Calendar.Date import *
from Utile.Calendar.Time import *


######################################################################################################################
############################## Class TimeTo ########################################################################
######################################################################################################################

class TimeTo:
    NumberOfDays: int = 0
    NumberOfHours: int = 0
    NumberOfMinutes: int = 0
    NumberOfSeconds: int = 0

    def __init__(self, numberOfDays: int = 0,
                 numberOfHours: int = 0,
                 numberOfMinutes: int = 0,
                 numberOfSeconds: int = 0) -> None:
        """
        Constructor of the class TimeTo
        :param numberOfDays: int
        :param numberOfHours: int
        :param numberOfMinutes: int
        :param numberOfSeconds: int
        """
        self.NumberOfDays = numberOfDays
        self.NumberOfHours = numberOfHours
        self.NumberOfMinutes = numberOfMinutes
        self.NumberOfSeconds = numberOfSeconds

    def __str__(self) -> str:
        """
        String representation of the class TimeTo
        :return: str
        """
        return str(self.NumberOfDays) + " days, " + \
               str(self.NumberOfHours) + " hours, " + \
               str(self.NumberOfMinutes) + " minutes, " + \
               str(self.NumberOfSeconds) + " seconds"

    def __eq__(self, other) -> bool:
        """
        Compare two times
        :param other: TimeTo
        :return: bool
        """
        # if other is a TimeTo
        if isinstance(other, TimeTo):
            return self.NumberOfDays == other.NumberOfDays \
                   and self.NumberOfHours == other.NumberOfHours \
                   and self.NumberOfMinutes == other.NumberOfMinutes \
                   and self.NumberOfSeconds == other.NumberOfSeconds
        else:
            return False


######################################################################################################################
############################## Special Functions #####################################################################
######################################################################################################################

def dayToTimeTo(NumberOfDays: int) -> TimeTo:
    """
    Convert a day to a time to
    :param day: Day
    :return: TimeTo
    """
    return TimeTo(numberOfDays=NumberOfDays)


def TimeToTimeTo(time: Time) -> TimeTo:
    """
    Convert a time to a time to
    :param time: Time
    :return: TimeTo
    """
    return TimeTo(numberOfHours=time.Hours,
                  numberOfMinutes=time.Minutes,
                  numberOfSeconds=time.Seconds)


def combineDayAndTimeInTimeTo(NumberOfDays: int, time: Time) -> TimeTo:
    """
    Combine a day and a time in a time to
    :param day: Day
    :param time: Time
    :return: TimeTo
    """
    return TimeTo(numberOfDays=NumberOfDays,
                  numberOfHours=time.Hours,
                  numberOfMinutes=time.Minutes,
                  numberOfSeconds=time.Seconds)

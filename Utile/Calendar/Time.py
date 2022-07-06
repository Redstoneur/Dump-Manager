import datetime as dt


######################################################################################################################
############################## Class Time ############################################################################
######################################################################################################################

class Time:
    Hours: int = 0
    Minutes: int = 0
    Seconds: int = 0
    Milliseconds: int = 0
    Microseconds: int = 0
    Nanoseconds: int = 0

    def __init__(self, hours: int = Hours, minutes: int = Minutes, seconds: int = Seconds,
                 milliseconds: int = Milliseconds, microseconds: int = Microseconds, nanoseconds: int = Nanoseconds) -> None:
        """
        Constructor of the class Time
        :param hours: int
        :param minutes: int
        :param seconds: int
        :param milliseconds: int
        :param microseconds: int
        :param nanoseconds: int
        """
        self.Hours = hours
        self.Minutes = minutes
        self.Seconds = seconds
        self.Milliseconds = milliseconds
        self.Microseconds = microseconds
        self.Nanoseconds = nanoseconds

    def setActualTime(self) -> None:
        """
        Set the actual time
        :return: None
        """
        now = dt.datetime.now()
        self.Hours = now.hour
        self.Minutes = now.minute
        self.Seconds = now.second
        self.Milliseconds = now.microsecond // 1000
        self.Microseconds = now.microsecond % 1000
        self.Nanoseconds = now.microsecond % 1000000

    def __str__(self) -> str:
        """
        String representation of the class Time
        :return: str
        """
        return str(self.Hours) + ":" + str(self.Minutes) + ":" + str(self.Seconds) + ":" + str(
            self.Milliseconds) + ":" + str(self.Microseconds) + ":" + str(self.Nanoseconds)

    def __eq__(self, other) -> bool:
        """
        Compare two times
        :param other: Time
        :return: bool
        """
        # if other is a Time
        if isinstance(other, Time):
            return self.Hours == other.Hours and self.Minutes == other.Minutes and self.Seconds == other.Seconds and \
                   self.Milliseconds == other.Milliseconds and self.Microseconds == other.Microseconds and \
                   self.Nanoseconds == other.Nanoseconds
        else:
            return False


######################################################################################################################
############################## Special Functions #####################################################################
######################################################################################################################

def getactualTime() -> Time:
    """
    Get the actual time
    :return: Time
    """
    time = Time()
    time.setActualTime()
    return time

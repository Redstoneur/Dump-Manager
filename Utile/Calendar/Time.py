import time as t


######################################################################################################################
############################## Class Time ############################################################################
######################################################################################################################

class Time:
    Hours: int = 0
    Minutes: int = 0
    Seconds: int = 0

    def __init__(self, hours: int = Hours, minutes: int = Minutes, seconds: int = Seconds) -> None:
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

    def setActualTime(self) -> None:
        """
        Set the actual time
        :return: None
        """
        now: t.struct_time = t.localtime()
        # hours
        self.Hours = now.tm_hour
        # minutes
        self.Minutes = now.tm_min
        # seconds
        self.Seconds = now.tm_sec

    def __str__(self) -> str:
        """
        String representation of the class Time
        :return: str
        """
        hours: str = "0" + str(self.Hours) if self.Hours < 10 else str(self.Hours)
        minutes: str = "0" + str(self.Minutes) if self.Minutes < 10 else str(self.Minutes)
        seconds: str = "0" + str(self.Seconds) if self.Seconds < 10 else str(self.Seconds)
        return hours + ":" + minutes + ":" + seconds

    def __eq__(self, other) -> bool:
        """
        Compare two times
        :param other: Time
        :return: bool
        """
        # if other is a Time
        if isinstance(other, Time):
            return self.Hours == other.Hours and self.Minutes == other.Minutes and self.Seconds == other.Seconds
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

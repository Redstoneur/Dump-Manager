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

    def timeToSeconds(self) -> int:
        """
        Convert time to seconds
        :return: int
        """
        return self.Hours * 3600 + self.Minutes * 60 + self.Seconds

    def secondsToTime(self, seconds: int) -> None:
        """
        Convert seconds to time
        :param seconds: int
        :return: None
        """
        self.Hours = seconds // 3600
        self.Minutes = (seconds % 3600) // 60
        self.Seconds = (seconds % 3600) % 60

    def anterior(self, other) -> bool:
        """
        Compare two times
        :param other: Time
        :return: bool
        """
        return self.timeToSeconds() < other.timeToSeconds()

    def posterior(self, other) -> bool:
        """
        Compare two times
        :param other: Time
        :return: bool
        """
        return self.timeToSeconds() > other.timeToSeconds()

    def differenceInSeconds(self, other) -> int | None:
        """
        Difference between two times in seconds
        :param other: Time
        :return: int
        """
        if isinstance(other, Time):
            # if the times are the same
            if self == other:
                return 0
            # if the first time is posterior to the second
            elif self.posterior(other):
                return self.timeToSeconds() - other.timeToSeconds()
            # if the first time is anterior to the second
            else:
                return other.timeToSeconds() - self.timeToSeconds()
        return None

    def differenceInTime(self, other):
        """
        Difference between two times in time
        :param other: Time
        :return: Time
        """
        secondes: int = self.differenceInSeconds(other)
        if secondes is not None:
            time: Time = Time()
            time.secondsToTime(secondes)
            return time
        return None


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

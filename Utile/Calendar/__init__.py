from Utile.Calendar.Date import *
from Utile.Calendar.Time import *
from Utile.Calendar.DateTime import *
from Utile.Calendar.WeekDay import *
from Utile.Calendar.Calendar import *


######################################################################################################################
############################## Class Error Calendar ##################################################################
######################################################################################################################

class ErrorCalendar(Calendar):
    start: WeekDay = None
    end: WeekDay = None
    timeLoaded: TimeTo = None
    content: str = ""

    def __init__(self, title: str, description: str = "",
                 content: str = "", date: Date = None, start: WeekDay = None, end: WeekDay = None) -> None:
        """
        Constructor of the class ErrorCalendar
        :param title: str
        :param description: str
        :param content: str
        :param date: Date
        :param start: WeekDay
        :param end: WeekDay
        """
        super().__init__(title=title, description=description, date=date)
        self.content = content
        if start is None:
            self.start = getActualWeekDay()
        else:
            self.start = start

        if end is None:
            self.end = getActualWeekDay()
        else:
            self.end = end

        self.timeLoaded = self.start.dateTime.differanceInTimeTo(self.end.dateTime)

    def __str__(self) -> str:
        """
        String representation of the class ErrorCalendar
        :return: str
        """
        return "Date: " + self.Date.__str__() + "\n" + \
               "Title: " + self.Title + "\n" + \
               "Description: " + self.Description + "\n" + \
               "Start: " + self.start.__str__() + "\n" + \
               "End: " + self.end.__str__() + "\n" + \
               "Time loaded: " + self.timeLoaded.__str__() + "\n" + \
               "Content: " + self.content + "\n"

    def __eq__(self, other) -> bool:
        """
        Compare two ErrorCalendar objects
        :param other: ErrorCalendar
        :return: bool
        """
        if isinstance(other, ErrorCalendar):
            return self.Date.__eq__(other.Date) \
                   and self.Title == other.Title \
                   and self.Description == other.Description \
                   and self.content == other.content \
                   and self.start.__eq__(other.start) \
                   and self.end.__eq__(other.end)
        else:
            return False

    def setStart(self, start: WeekDay) -> None:
        """
        Set the start of the error
        :param start: WeekDay
        :return: None
        """
        self.start = start
        self.timeLoaded = self.start.dateTime.differanceInTimeTo(self.end.dateTime)

    def setEnd(self, end: WeekDay) -> None:
        """
        Set the end of the error
        :param end: WeekDay
        :return: None
        """
        self.end = end
        self.timeLoaded = self.start.dateTime.differanceInTimeTo(self.end.dateTime)

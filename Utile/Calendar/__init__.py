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
            self.start = WeekDay()
        else:
            self.start = start

        if end is None:
            self.end = WeekDay()
        else:
            self.end = end

    def __str__(self) -> str:
        """
        String representation of the class ErrorCalendar
        :return: str
        """
        return "Date: " + self.Date.__str__() + "\n" + \
               "Title: " + self.Title + "\n" + \
               "Description: " + self.Description + "\n" + \
               "Content: " + self.content + "\n" \
               "Start: " + self.start.__str__() + "\n" \
               "End: " + self.end.__str__() + "\n"

    def __eq__(self, other) -> bool:
        """
        Compare two ErrorCalendar objects
        :param other: ErrorCalendar
        :return: bool
        """
        if isinstance(other, ErrorCalendar):
            return self.Date == other.Date \
                   and self.Title == other.Title \
                   and self.Description == other.Description \
                   and self.content == other.content \
                   and self.start == other.start \
                   and self.end == other.end
        else:
            return False

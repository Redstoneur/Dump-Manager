from Utile.Calendar.Date import *
from Utile.Calendar.Time import *
from Utile.Calendar.DateTime import *
from Utile.Calendar.WeekDay import *


######################################################################################################################
############################## Class Calendar ########################################################################
######################################################################################################################

class Calendar:
    WeekDay: WeekDay = None
    Title: str = ""
    Description: str = ""
    Content: str = ""
    src: str = ""
    dst: str = ""

    def __init__(self, title: str, description: str = Description,
                 content: str = Content, src: str = src, dst: str = dst, weekDay: WeekDay = None) -> None:
        """
        Constructor of the class Calendar
        :param weekDay: WeekDay
        :param title: str
        :param description: str
        :param content: str
        :param src: str
        :param dst: str
        """
        self.Title = title
        self.Description = description
        self.Content = content
        self.src = src
        self.dst = dst

        if weekDay is None:
            self.WeekDay = getActualWeekDay()
        else:
            self.WeekDay = weekDay

    def setActualCalendar(self) -> None:
        """
        Set the actual calendar
        :return: None
        """
        self.WeekDay.setActualWeekDay()

    def __str__(self) -> str:
        """
        String representation of the class Calendar
        :return: str
        """
        return "WeekDay: " + self.WeekDay.__str__() + "\n" + \
               "Title: " + self.Title + "\n" + \
               "Description: " + self.Description + "\n" + \
               "Content: " + self.Content + "\n"

    def __eq__(self, other) -> bool:
        """
        Compare two calendars
        :param other: Calendar
        :return: bool
        """
        # if other is a Calendar
        if isinstance(other, Calendar):
            return self.WeekDay == other.WeekDay \
                   and self.Title == other.Title \
                   and self.Description == other.Description \
                   and self.Content == other.Content \
                   and self.src == other.src \
                   and self.dst == other.dst
        else:
            return False

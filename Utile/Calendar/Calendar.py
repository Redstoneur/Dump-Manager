from Utile.Calendar.WeekDay import *
from abc import abstractmethod, ABC


######################################################################################################################
############################## Class Calendar ########################################################################
######################################################################################################################

class Calendar(ABC):
    Date = None
    Title: str = ""
    Description: str = ""

    @abstractmethod
    def __init__(self,
                 title: str,
                 description: str = Description,
                 date: Date = None
                 ) -> None:
        """
        Constructor of the class Calendar
        :param title: str
        :param description: str
        :param date: Date
        """
        self.Title = title
        self.Description = description

        if date is None:
            self.Date = Date()
        else:
            self.Date = date

    def setActualCalendar(self) -> None:
        """
        Set the actual calendar
        :return: None
        """
        self.Date.setActualWeekDay()

    def __str__(self) -> str:
        """
        String representation of the class Calendar
        :return: str
        """
        return "Date: " + self.Date.__str__() + "\n" + \
               "Title: " + self.Title + "\n" + \
               "Description: " + self.Description + "\n"

    def __eq__(self, other) -> bool:
        """
        Compare two calendars
        :param other: Calendar
        :return: bool
        """
        # if other is a Calendar
        if isinstance(other, Calendar):
            return self.Date == other.Date \
                   and self.Title == other.Title \
                   and self.Description == other.Description
        else:
            return False

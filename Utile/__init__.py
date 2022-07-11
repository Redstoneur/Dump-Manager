from Utile.Calendar import *
from Utile.FileAndFolder import *


######################################################################################################################
############################## Class Error ###########################################################################
######################################################################################################################

class Error:
    messageFormat: dict[str] = {"s": "success: ", "m": "message: ", "c": "code: "}
    dataFormatSpace: str = "@space"
    formatSpace: str = " " * len(messageFormat["m"])
    success: bool = True
    message: str = "success"
    code: int = 200

    def __init__(self, success: bool, message: str, code: int) -> None:
        """
        create a Error object
        :param success: bool, success of the error
        :param message: str, message of the error
        :param code: int, code of the error
        """
        self.success: bool = success
        self.message: str = message
        self.code: int = code

    def __str__(self) -> str:
        """
        get the Error object as a string
        :return: str, Error object as a string
        """
        return self.messageFormat["s"] + str(self.success) + "\n" + \
               self.messageFormat["m"] + self.message.replace(self.dataFormatSpace, self.formatSpace) + "\n" + \
               self.messageFormat["c"] + str(self.code)

    def get_message(self, space: str = None) -> str:
        """
        get the message of the error with the space format
        :param space: str, space to format the message
        :return: str, message of the error with the space format
        """
        if isinstance(space, str):
            return self.messageFormat["m"] + self.message.replace(self.dataFormatSpace, self.formatSpace + space)
        return self.messageFormat["m"] + self.message.replace(self.dataFormatSpace, self.formatSpace)

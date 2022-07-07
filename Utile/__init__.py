from Utile.Calendar import *
from Utile.FileAndFolder import *


class Error:
    success: bool = True
    message: str = "success"
    code: int = 200

    def __init__(self, success: bool, message: str, code: int) -> None:
        self.success: bool = success
        self.message: str = message
        self.code: int = code

    def __str__(self) -> str:
        return "success: " + str(self.success) + "\n" + \
               "message: " + self.message + "\n" + \
               "code: " + str(self.code)

    def line(self) -> str:
        return "success: " + str(self.success) + " | message: " + self.message + \
                       " | code: " + str(self.code)

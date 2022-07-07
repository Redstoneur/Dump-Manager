import sys
from Utile import *

from DevFileManager import *
from Runner import *


def main(run: str = "nothing") -> Error:
    """
    main function of the program
    :param run: str, information or dump
    :return: Error, error object
    """
    error: Error

    if information():  # if read information
        if run == "shell":  # if run shell
            error: Error = ShellRunner()
        elif run == "db":  # if run database
            error = DbRunner()
        else:  # if run nothing
            error = Error(success=False, message="run not found", code=3)
    else:  # if not read information
        error = Error(success=False, message="Error: information", code=4)

    # create a file with a Calendar of the last dump
    CalendarFileManager(error)

    # create a file log with the error
    LogFileManager(error)

    return error


if __name__ == '__main__':
    # recuperation of the arguments
    if len(sys.argv) > 1:
        run = sys.argv[1]
    else:
        run = "shell"

    # run the program
    result: Error = main(run=run)

    # if in debug mode, wait for the user to press a key
    if not result.success and result.code != 200:
        print("\n" + result.__str__() + "\n")
        input("Press Enter to continue...")
        sys.exit(result.code)
    else:
        sys.exit(result.code)

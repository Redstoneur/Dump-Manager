import sys
from Database import mainVersionDB
from Utile import Error
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
            error = mainVersionDB()
        else:  # if run nothing
            error = Error(success=False, message="run not found", code=3)
    else:  # if not read information
        error = Error(success=False, message="Error: information", code=4)

    # create a file with a Calendar of the last dump
    print("\nCreating Calendar of the last dump")
    try:  # try to create a file with a Calendar of the last dump
        f: file = generateFile(path="./Data/calendar.txt", sp='engineer', debug=True)
        if isinstance(f, TxtFile):  # if the file is a TxtFile
            txt: TxtFile = TxtFile(path=f.getPath())
            calendar: Calendar = Calendar(title="Dumps",
                                          description="Dumps of the databases",
                                          content=result.line())
            txt.__add__(data="\n#####################################################"
                             "#######################################\n\n " + calendar.__str__())
            print("Calendar created")
        else:  # if not a TxtFile
            print("Error: calendar")
    except Exception as e:  # if not create a file with a Calendar of the last dump
        print(e)
        print("Error: calendar")
    else:  # if create a file with a Calendar of the last dump
        print("Calendar script finished")

    # create a file log with the error
    print("\nCreating log file")
    try:  # try to create a file log with the error
        f: file = generateFile(path="./Data/log.txt", sp='engineer', debug=True)
        if isinstance(f, TxtFile):  # if the file is a TxtFile
            txt: TxtFile = TxtFile(path=f.getPath())
            txt.write(data=result.__str__())
            print("Log file created")
        else:  # if not a TxtFile
            print("Error: log")
    except Exception as e:  # if not create a file log with the error
        print(e)
        print("Error: can't create log file")
    else:  # if create a file log with the error
        print("Log file script finished")

    print("\n")

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

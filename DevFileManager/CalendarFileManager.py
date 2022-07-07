from Utile import *


def CalendarFileManager(error: Error) -> Error:
    """
    Create and modify a file with a Calendar of the last dump
    :param error: Error, error object
    :return: None
    """
    result: Error

    print("\nCreating Calendar of the last dump")

    try:  # try to create a file with a Calendar of the last dump

        f: file = generateFile(path="./Data/calendar.txt", sp='engineer', debug=True)  # create or verify the file

        if isinstance(f, TxtFile):  # if the file is a TxtFile
            txt: TxtFile = TxtFile(path=f.getPath())  # create a TxtFile object with the file
            calendar: Calendar = Calendar(title="Dumps",
                                          description="Dumps of the databases",
                                          content=error.line())  # create a Calendar object with the error

            # add the Calendar to the file
            txt.__add__(data="\n#####################################################"
                             "#######################################\n\n " + calendar.__str__())

            print("Calendar created")
            result = Error(success=True, message="Calendar created", code=0)
        else:  # if not a TxtFile
            print("Error: calendar")
            result = Error(success=False,
                           message="Error: can't add Calendar to the file",
                           code=1)

    except Exception as e:  # if not create a file with a Calendar of the last dump
        print(e)
        print("Error: calendar")
        result = Error(success=False,
                       message="Error: problem with the file",
                       code=2)
    else:  # if create a file with a Calendar of the last dump
        if result.success:
            print("Calendar script finished")

    print("\n")

    return result

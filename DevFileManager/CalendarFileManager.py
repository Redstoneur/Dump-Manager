from Utile import *


######################################################################################################################
############################## Calendar File Manager #################################################################
######################################################################################################################

def CalendarFileManager(start: WeekDay, error: Error) -> Error:
    """
    Create and modify a file with a Calendar of the last dump
    :param error: Error, error object
    :return: None
    """
    result: Error
    b: bool = True
    path: str = "./Data/calendar.txt"

    print("\nCreating Calendar of the last dump")

    try:  # try to create a file with a Calendar of the last dump

        f: file = generateFile(path=path, sp='engineer', debug=True)  # create or verify the file

        if f is None:  # if the file is a TxtFile
            print("Generating " + path)
            b: bool = createTxtFile(path)  # create a TxtFile object with the file
            f: file = generateFile(path=path, sp='engineer', debug=True)  # create or verify the file

        if isinstance(f, TxtFile) and b:  # if the file is a TxtFile
            txt: TxtFile = TxtFile(path=f.getPath())  # create a TxtFile object with the file



            # create the content of calendar

            space: str = " " * len("Content: ")
            content: str = "\n" + \
                           space + "- success: " + str(error.success) + "\n" + \
                           space + "- " + error.get_message(space) + "\n" + \
                           space + "- code: " + str(error.code) + "\n"

            # create the calendar of the last dump
            calendar: ErrorCalendar = ErrorCalendar(title="Dumps",
                                                    description="Dumps of the databases",
                                                    date=start.dateTime.Date,
                                                    start=start,
                                                    content=content)  # create a Calendar object with the error

            if txt.data == "":  # if not have data in the file
                # put the Calendar in the file
                txt.write(data=calendar.__str__())

            else:  # if have data in the file
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

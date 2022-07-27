from Utilities import *


######################################################################################################################
############################## Calendar File Manager #################################################################
######################################################################################################################

def CalendarFileManager(titre: str, description: str, start: WeekDay, error: Error, graphique: bool) -> Error:
    """
    Create and modify a file with a Calendar of the last dump
    :param titre: str, title of the Calendar
    :param description: str, description of the Calendar
    :param start: WeekDay, start of the Calendar
    :param error: Error, error object
    :param graphique: bool, True if we want to run the program in graphique mode
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

            # create the calendar of the last dump
            calendar: ErrorCalendar = CreateCalendar(titre=titre,
                                                     description=description,
                                                     start=start,
                                                     error=error,
                                                     graphique=graphique)

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


def CreateCalendar(titre: str, description: str, start: WeekDay, error: Error, graphique: bool) -> ErrorCalendar:
    """
    Create and modify a file with a Calendar of the last dump
    :param titre: str, title of the Calendar
    :param description: str, description of the Calendar
    :param start: WeekDay, start of the Calendar
    :param error: Error, error object
    :param graphique: bool, True if we want to run the program in graphique mode
    :return: None
    """
    # create the content of calendar
    space: str = " " * len("Content: ")
    grapher: str = space + "Mode graphique\n" if graphique else space + "Mode console\n"
    content: str = "\n" + \
                   grapher + \
                   space + "- success: " + str(error.success) + "\n" + \
                   space + "- " + error.get_message(space) + "\n" + \
                   space + "- code: " + str(error.code) + "\n"

    # create the calendar of the last dump
    calendar: ErrorCalendar = ErrorCalendar(title=titre,
                                            description=description,
                                            date=start.dateTime.Date,
                                            start=start,
                                            content=content)  # create a Calendar object with the error

    return calendar

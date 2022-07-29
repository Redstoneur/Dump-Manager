from Utilities import Error, TxtFile, generateFile, createTxtFile, file


######################################################################################################################
############################## Log File Manager ######################################################################
######################################################################################################################

def LogFileManager(error: Error) -> Error:
    """
    Create and modify a file with the log of the last dump
    :param error: Error, error object
    :return: None
    """
    result: Error
    b: bool = True
    path: str = "./Variable/log.txt"

    print("\nCreating log file")

    try:  # try to create a file log with the error

        f: file = generateFile(path=path, sp='engineer', debug=True)  # create or verify the file

        if f is None:  # if the file is a TxtFile
            print("Generating " + path)
            b: bool = createTxtFile(path)  # create a TxtFile object with the file
            f: file = generateFile(path=path, sp='engineer', debug=True)  # create or verify the file

        if isinstance(f, TxtFile) and b:  # if the file is a TxtFile
            txt: TxtFile = TxtFile(path=f.getPath())  # create a TxtFile object with the file
            txt.write(data=error.__str__())  # write the error in the file

            print("Log file created")
            result = Error(success=True, message="Log file created", code=0)
        else:  # if not a TxtFile
            print("Error: log")
            result = Error(success=False,
                           message="Error: can't add log to the file",
                           code=1)
    except Exception as e:  # if not create a file log with the error
        print(e)
        print("Error: can't create log file")
        result = Error(success=False,
                       message="Error: problem with the file",
                       code=2)
    else:  # if create a file log with the error
        if result.success:
            print("Log file script finished")

    print("\n")

    return result

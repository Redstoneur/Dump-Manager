import sys
from Utile import *

######################################################################################################################
############################## Shell Runner ##########################################################################
######################################################################################################################

DatabaseInfo: JsonFile = JsonFile("./Data/Database-Information.json")

# noinspection PyTypeChecker
DumpsPath: str = DatabaseInfo.get("path-dumps")
if DumpsPath is None or DumpsPath == "":
    DumpsPath = "./Data/Dumps"
FoldersContained: FoldersContained = FoldersContained(DumpsPath)

# noinspection PyTypeChecker
shellStartCommand: str = DatabaseInfo.get("script-dumps")
if shellStartCommand is None or shellStartCommand == "":
    print(Error(success=False, message="Error: not have script-dumps in Database-Information.json", code=1).__str__())
    sys.exit(1)
elif "@user" not in shellStartCommand or "@pw" not in shellStartCommand or "@dump" not in shellStartCommand:
    print(Error(success=False, message="Error: not have @user, @pw, @dump in shellStartCommand", code=2).__str__())
    sys.exit(2)


def ShellRunner(loadDumps: str = 'all dumps') -> Error:
    """
    dump all databases with a shell command
    :return: bool, True if the program worked, False if not
    """
    print("Dump started")

    error: Error
    numbersOfDumps: int = 0
    numbersOfDumpsSuccess: int = 0
    numbersOfDumpsError: int = 0
    numbersOfFiles: int = 0
    listOfDumps: list[str] = []
    success: bool = True
    message: str = "success"
    code: int = 200

    # get all dumps in the folder and add them to the server with a shell command to load the dump in the database
    for folder in FoldersContained.folders:
        numbersOfFiles += 1

        # don't read Dumps.md
        if folder == "Dumps.md":
            continue

        # create variables file to use in shell command of dump
        f = generateFile(path=DumpsPath + "/" + folder, sp='Dump', debug=True)

        if f is not None and f.getExtension() == "sql":  # if the file is a sql file

            sql: dumpSqlFile = dumpSqlFile(path=DumpsPath + "/" + folder)

            if loadDumps != "all dumps" and loadDumps != sql.getNameDataBase():
                continue
            else:
                listOfDumps += [sql.getNameDataBase()]

            print("Dumping: " + sql.getNameDataBase() + " (Date of dump: " + sql.getDateOfDump() + ")")

            # shell command
            # shellStartCommand = "docker exec -i mysql mysql -u @user -p@pw < @dump"
            # replace @user and @pw with the user and password of the database
            # replace @dump with the path of the dump file
            # replace @dump with the path of the dump file

            # noinspection PyTypeChecker
            command = shellStartCommand.replace("@user", DatabaseInfo.get("user"))
            # noinspection PyTypeChecker
            command = command.replace("@pw", DatabaseInfo.get("password"))
            command = command.replace("@dump", sql.getPath())

            print("Executing: " + command)

            # execute shell command
            try:
                os.system(command)
            except Exception as e:
                if success:
                    success = False
                    message = "Error to dump\n"
                    code = 406
                message += "\n" + str(e)
                print("Error: " + str(e))
                numbersOfDumpsError += 1
            else:
                numbersOfDumpsSuccess += 1
                print("Dump success")

            print("Executed: " + sql.getNameDataBase() + "\n")

            numbersOfDumps += 1

        elif f is not None and f.getExtension() != "sql":  # if the file is not a sql file
            if success:
                success = False
                message = "Error: not a sql file\n"
                code = 405
            message += "\n" + f.getName() + " is not a sql file"
        else:  # if the file is not found
            if success:
                success = False
                message = "Error to dump\n"
                code = 404
            message += "\nError: folder " + folder + " is not a database dump"
            print("Error: folder " + folder + " is not a database dump")

    print("Dump finished")

    if loadDumps != "all dumps":
        data: str = "@space-> Dump: " + listOfDumps[0]
    else:
        data: str = "@space-> Dumps: " + str(listOfDumps) + "\n" + \
                    "@space-> Dumps: " + str(numbersOfDumps) + "\n" + \
                    "@space-> Dumps success: " + str(numbersOfDumpsSuccess) + "\n" + \
                    "@space-> Dumps error: " + str(numbersOfDumpsError) + "\n" + \
                    "@space-> Files: " + str(numbersOfFiles)

    return Error(success=success, message=message + "\n" + data, code=code)


def ListOfDumps() -> list[str]:
    """
    list all dumps in the folder
    :return: list[str], list of all dumps in the folder
    """
    listOfDumps: list[str] = ['all dumps']
    for folder in FoldersContained.folders:
        if folder == "Dumps.md":
            continue
        else:
            f = generateFile(path=DumpsPath + "/" + folder, sp='Dump', debug=True)
            if f is not None and f.getExtension() == "sql":  # if the file is a sql file
                sql: dumpSqlFile = dumpSqlFile(path=DumpsPath + "/" + folder)
                listOfDumps += [sql.getNameDataBase()]
    return listOfDumps

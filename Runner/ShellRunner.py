import sys
from FileAndFolder import *
from Utile import *

DatabaseInfo: JsonFile = JsonFile("./Data/Database-Information.json")

# noinspection PyTypeChecker
DumpsPath: str = DatabaseInfo.get("path-dumps")
if DumpsPath is None or DumpsPath == "":
    DumpsPath = "./Data/Dumps"
    print(DumpsPath)
FoldersContained: FoldersContained = FoldersContained(DumpsPath)

# noinspection PyTypeChecker
shellStartCommand: str = DatabaseInfo.get("script-dumps")
if shellStartCommand is None or shellStartCommand == "":
    print(Error(success=False, message="Error: not have script-dumps in Database-Information.json", code=1).__str__())
    sys.exit(1)
elif "@user" not in shellStartCommand or "@pw" not in shellStartCommand or "@dump" not in shellStartCommand:
    print(Error(success=False, message="Error: not have @user, @pw, @dump in shellStartCommand", code=2).__str__())
    sys.exit(2)


def ShellRunner() -> Error:
    """
    dump all databases with a shell command
    :return: bool, True if the program worked, False if not
    """
    print("Dump started")

    error: Error
    success: bool = True
    message: str = "success"
    code: int = 200

    # get all dumps in the folder and add them to the server with a shell command to load the dump in the database
    for folder in FoldersContained.folders:

        # don't read Dumps.md
        if folder == "Dumps.md":
            continue

        # create variables file to use in shell command of dump
        f = generateFile(path=DumpsPath + "/" + folder, sp='Dump', debug=True)

        if f is not None and f.getExtension() == "sql":

            sql: dumpSqlFile = dumpSqlFile(path=DumpsPath + "/" + folder)

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

            print("Executed: " + sql.getNameDataBase() + "\n")

        elif f is not None and f.getExtension() != "sql":
            if success:
                success = False
                message = "Error: not a sql file\n"
                code = 405
            message += "\n" + f.getName() + " is not a sql file"
        else:
            if success:
                success = False
                message = "Error to dump\n"
                code = 404
            message += "\nError: folder " + folder + " is not a database dump"
            print("Error: folder " + folder + " is not a database dump")

    print("Dump finished")
    return Error(success, message, code)

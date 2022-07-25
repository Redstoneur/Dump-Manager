import sys
import tkinter as tk
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
elif DatabaseInfo.get("doker_container") is not None and DatabaseInfo.get("doker_container") != "":
    if "@doker_container" not in shellStartCommand:
        print(Error(success=False, message="Error: not have @doker_container in shellStartCommand", code=3).__str__())
        sys.exit(3)

ignoredFiles: list[str] = [".Dumps.md", "lastDumpsFiles"]


def isDockerCommand(command: str) -> bool:
    """
    check if the command is a docker command
    :param command: str, command to check
    :return: bool, True if the command is a docker command, False if not
    """
    if "@doker_container" in command:
        return True
    return False


def get_default_docker_container() -> str | None:
    """
    get the default docker container
    :return: str, default
    """
    if isDockerCommand(shellStartCommand) and DatabaseInfo.get("doker_container") is not None and DatabaseInfo.get(
            "doker_container") != "":
        return str(DatabaseInfo.get("doker_container"))
    else:
        return None


def ignoredFile(txt: str):
    """
    check if the file is ignored
    :param txt: str, name of the file
    :return: bool, True if the file is ignored, False if not
    """
    for i in ignoredFiles:
        if i == txt:
            return True
    return False


def ShellRunner(loadingLabel: tk.Label = None, textfieldDockerContainer: tk.Text = None,
                loadDumps: str = 'all dumps') -> Error:
    """
    dump all databases with a shell command
    :return: bool, True if the program worked, False if not
    """
    print("Dump started")
    numbersOfDumpsTheoretical: int = NumberOfDumps()
    FoldersContained.update()

    error: Error
    listOfDumps: list[str] = []
    numbersOfDumps: int = 0
    listOfDumpsSuccess: list[str] = []
    numbersOfDumpsSuccess: int = 0
    listOfDumpsError: list[str] = []
    numbersOfDumpsError: int = 0
    numbersOfFiles: int = 0

    success: bool = True
    message: str = "success"
    code: int = 200

    # check if is a docker command and get the docker container if is necessary
    # noinspection PyTypeChecker
    NameDockerContainer: str = get_default_docker_container()
    if NameDockerContainer is not None:  # if is a docker command
        Name: str = textfieldDockerContainer.get("1.0",
                                                 "end-1c")  # get the name of the docker container from the textfield
        if Name == "":  # if the name is empty
            textfieldDockerContainer.insert("1.0", NameDockerContainer)  # insert the default name
        else:  # if the name is not empty
            NameDockerContainer = Name  # set the name of the docker container

        print("Docker container: " + NameDockerContainer)

    # get all dumps in the folder and add them to the server with a shell command to load the dump in the database
    for folder in FoldersContained.folders:

        # don't read .Dumps.md
        if ignoredFile(folder):
            continue
        else:
            numbersOfFiles += 1

        # create variables file to use in shell command of dump
        f = generateFile(path=DumpsPath + "/" + folder, sp='Dump', debug=True)

        if f is not None and f.getExtension() == "sql":  # if the file is a sql file

            sql: dumpSqlFile = dumpSqlFile(path=DumpsPath + "/" + folder)

            if loadDumps != "all dumps" and loadDumps != sql.getNameDataBase():
                continue
            else:
                numbersOfDumps += 1
                listOfDumps += [sql.getNameDataBase()]
                if loadingLabel is not None:
                    text: str = "Dump in running: " + sql.getNameDataBase()
                    if loadDumps == "all dumps":
                        text += " (" + str(numbersOfDumps) + "/" + str(numbersOfDumpsTheoretical) + ")"
                    loadingLabel.config(text=text)
                    loadingLabel.update()

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
            if NameDockerContainer is not None:  # if is a docker command and have a docker container name to use it
                command = command.replace("@doker_container", NameDockerContainer)

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
                listOfDumpsError += [sql.getNameDataBase()]
            else:
                numbersOfDumpsSuccess += 1
                listOfDumpsSuccess += [sql.getNameDataBase()]
                print("Dump success")

            print("Executed: " + sql.getNameDataBase() + "\n")


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
        if len(listOfDumps) == 0:
            listOfDumps = ["No dumps"]
        data: str = "@space-> Dump: " + listOfDumps[0]
    else:
        data: str = "@space-> Dumps: " + str(numbersOfDumps) + " | " + str(listOfDumps) + "\n" + \
                    "@space-> Dumps success: " + str(numbersOfDumpsSuccess) + " | " + str(listOfDumpsSuccess) + "\n" + \
                    "@space-> Dumps error: " + str(numbersOfDumpsError) + " | " + str(listOfDumpsError) + "\n" + \
                    "@space-> Files: " + str(numbersOfFiles)

    return Error(success=success, message=message + "\n" + data, code=code)


def ListOfDumps() -> list[str]:
    """
    list all dumps in the folder
    :return: list[str], list of all dumps in the folder
    """
    FoldersContained.update()
    listOfDumps: list[str] = ['all dumps']

    for folder in FoldersContained.folders:
        if ignoredFile(folder):
            continue
        else:
            f = generateFile(path=DumpsPath + "/" + folder, sp='Dump', debug=True)
            if f is not None and f.getExtension() == "sql":  # if the file is a sql file
                sql: dumpSqlFile = dumpSqlFile(path=DumpsPath + "/" + folder)
                listOfDumps += [sql.getNameDataBase() + " (" + sql.getDateOfDump() + ")"]
    return listOfDumps


def NumberOfDumps() -> int:
    """
    number of dumps in the folder
    :return: int, number of dumps in the folder
    """
    numbersOfDumps: int = 0
    FoldersContained.update()

    for folder in FoldersContained.folders:
        if ignoredFile(folder):
            continue
        else:
            f = generateFile(path=DumpsPath + "/" + folder, sp='Dump', debug=True)
            if f is not None and f.getExtension() == "sql":  # if the file is a sql file
                numbersOfDumps += 1
    return numbersOfDumps

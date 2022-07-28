import sys
from Runner.DevFileManager.ApplicationInformation import *
from Utilities import *


######################################################################################################################
############################## variables Shell Runner ################################################################
######################################################################################################################

def isDockerCommand(command: str) -> bool:
    """
    check if the command is a docker command
    :param command: str, command to check
    :return: bool, True if the command is a docker command, False if not
    """
    if "@doker_container" in command:
        return True
    return False


def verifyCommand(command: object, name: str, haveUser: bool, havePw: bool, haveDump: bool, haveDbName: bool) -> Error:
    """
    verify if the command is valid
    :param command: object, command to verify
    :param name: str, name of the command
    :param haveUser: bool, True if the command have a user, False if not
    :param havePw: bool, True if the command have a password, False if not
    :param haveDump: bool, True if the command have a dump, False if not
    :param haveDbName: bool, True if the command have a database name, False if not
    :return: Error, error with success = False if the command is not valid, success = True if the command is valid
    """
    error: Error = Error(success=True,
                         message="the command is valid",
                         code=200)

    if isinstance(command, str) and (command is not None or command != ""):
        command: str = str(command)
        if "@user" not in command and haveUser:
            error = Error(success=False, message="Error: not have @user in command (%s)" % name, code=2)
        elif "@pw" not in command and havePw:
            error = Error(success=False, message="Error: not have @pw in command (%s)" % name, code=3)
        elif "@dump" not in command and haveDump:
            error = Error(success=False, message="Error: not have @dump in command (%s)" % name, code=4)
        elif "@db" not in command and haveDbName:
            error = Error(success=False, message="Error: not have @db in command (%s)" % name, code=5)
        elif DatabaseInfo.get("doker_container") is not None and DatabaseInfo.get("doker_container") != "":
            if "@doker_container" not in command:
                error = Error(success=False, message="Error: not have @doker_container in command (%s)" % name, code=6)
        elif isDockerCommand(command):
            if DatabaseInfo.get("doker_container") is None or DatabaseInfo.get("doker_container") == "":
                error = Error(success=False, message="Error: not have doker_container (%s)" % name, code=7)
    else:
        error = Error(success=False, message="Error: not have script-dumps (%s)" % name, code=1)

    return error


def turnCommandeToExecutable(command: str, user: str, password: str, dump: str,
                             NameDockerContainer: str = None, db: str = None) -> str:
    """
    turn the command to executable
    :param command: str, command to turn
    :param user: str, user to use in the command
    :param password: str, password to use in the command
    :param dump: str, dump to use in the command
    :param NameDockerContainer: str, name of the docker container to use in the command
    :param db: str, database name to use in the command
    :return:
    """
    # replace @user and @pw with the user and password of the database
    command = command.replace("@user", user)
    # replace @pw with the password of the database
    command = command.replace("@pw", password)
    # replace @dump with the path of the dump file
    command = command.replace("@dump", dump)
    if db is not None:  # if the database name is not None
        # replace @db with the database name
        command = command.replace("@db", db)
    if NameDockerContainer is not None:  # if is a docker command and have a docker container name to use it
        # replace @doker_container with the docker container name
        command = command.replace("@doker_container", NameDockerContainer)
    return command


ApplicationInformation: ApplicationInformation = ApplicationInformation("./Data/package.json")
my_os: str = plt.system()
DatabaseInfo: JsonFile = JsonFile("./Data/Database-Information.json")

# noinspection PyTypeChecker
DumpsPath: str = DatabaseInfo.get("path-dumps")
if DumpsPath is None or DumpsPath == "":
    DumpsPath = "./Data/Dumps"
FoldersContained: FoldersContained = FoldersContained(DumpsPath)

AddDumpsCommand: str = str(DatabaseInfo.get("script-dumps"))
errorAddDumpsCommand: Error = verifyCommand(AddDumpsCommand, name="AddDumpsCommand", haveUser=True, havePw=True,
                                            haveDump=True, haveDbName=False)
if not errorAddDumpsCommand.success:
    print(errorAddDumpsCommand.__str__())
    sys.exit(errorAddDumpsCommand.code)

GenerateDumpCommand: str = str(DatabaseInfo.get("script-dumps-generator"))
errorGenerateDumpCommand: Error = verifyCommand(GenerateDumpCommand, name="GenerateDumpCommand", haveUser=True,
                                                havePw=True, haveDump=True, haveDbName=True)
if not errorGenerateDumpCommand.success:
    print(errorGenerateDumpCommand.__str__())
    sys.exit(errorGenerateDumpCommand.code)

ignoredFiles: list[str] = [".Dumps.md", "lastDumpsFiles"]

ignoredDatabases: list[str] = ["information_schema", "mysql", "performance_schema", "sys"]

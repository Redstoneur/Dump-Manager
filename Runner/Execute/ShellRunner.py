from Runner.LineFrame.DataManagerFrame import *
from Runner.Execute.varShellRunner import *


######################################################################################################################
############################## Shell Runner ##########################################################################
######################################################################################################################


def get_default_docker_container() -> str | None:
    """
    get the default docker container
    :return: str, default
    """
    if isDockerCommand(AddDumpsCommand) and DatabaseInfo.get("doker_container") is not None and DatabaseInfo.get(
            "doker_container") != "":
        return str(DatabaseInfo.get("doker_container"))
    else:
        return None


def get_default_user_name() -> str:
    """
    get the default user name
    :return: str, user name
    """
    return str(DatabaseInfo.get("user"))


def get_default_password() -> str:
    """
    get the default password
    :return: str, password
    """
    return str(DatabaseInfo.get("password"))


def get_docker_container(DockerFrame: DataManagerFrame) -> str | None:
    NameDockerContainer: str = DockerFrame.get_default()
    if NameDockerContainer is not None:  # if is a docker command
        Name: str = DockerFrame.get_textfield_value()
        if Name == "":  # if the name is empty
            DockerFrame.set_default(get_default_docker_container())
        else:  # if the name is not empty
            NameDockerContainer = Name  # set the name of the docker container

    return NameDockerContainer


def get_user_name(UserFrame: DataManagerFrame = None) -> str:
    """
    get the user name
    :return: str, user name
    """
    UserName: str = UserFrame.get_default()
    Name: str = UserFrame.get_textfield_value()
    if Name == "":  # if the name is empty
        UserFrame.set_default(get_default_user_name())
    else:  # if the name is not empty
        UserName = Name  # set the name of the user

    return UserName


def get_password(PasswordFrame: DataManagerFrame) -> str:
    """
    get the password
    :param PasswordFrame: DataManagerFrame, frame of the password
    :return: str, password
    """
    Password: str = PasswordFrame.get_default()
    value: str = PasswordFrame.get_textfield_value()
    if value == "":  # if the password is empty
        PasswordFrame.set_default(get_default_password())
    else:  # if the password is not empty
        Password = value  # set the password

    return Password


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


def listDatabases() -> list:
    try:
        db: DatabaseExecutor = DatabaseExecutor(user=str(DatabaseInfo.get("user")),
                                                password=str(DatabaseInfo.get("password")),
                                                host=str(DatabaseInfo.get("host")),
                                                port=int(str(DatabaseInfo.get("port"))))
        listDb = db.listDatabases()
        db.close()
    except Exception as e:
        print(Error(success=False, message="Error: %s" % str(e), code=1))
        return []
    return listDb


def ignoredDatabase(db: str) -> bool:
    """
    check if the database is ignored
    :param db: str, name of the database
    :return: bool, True if the database is ignored, False if not
    """
    for i in ignoredDatabases:
        if i == db:
            return True
    return False


def listDatabasesWithoutSytemBase() -> list:
    """
    list all databases without system base
    :return: list[str], list of all databases without system base
    """
    listDb: list[str] = []
    for db in listDatabases():
        if ignoredDatabase(db):
            continue
        else:
            listDb += [db]
    return listDb


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


def CleanDumpsFolder(loadingLabel: tk.Label = None, loadDumps="all dumps") -> Error:
    """
    clean the folder of all dumps
    :return: Error, error message
    """
    FoldersContained.update()
    success: bool = True
    message: str = "the folder is clean"
    code: int = 200

    pathLastDumpsFiles = DumpsPath + "/lastDumpsFiles"
    createFolder(pathLastDumpsFiles)

    print("Start cleaning the folder")
    loadingLabel.config(text="Start cleaning the folder")

    numFolders: int = 0

    for folder in FoldersContained.folders:
        if ignoredFile(folder):
            continue
        else:
            numFolders += 1
            print("Cleaning: " + folder)
            loadingLabel.config(
                text="Cleaning: " + folder + "(" + str(numFolders) + "/" + str(len(ListOfDumps())) + ")")
            f = generateFile(path=DumpsPath + "/" + folder, sp='Dump', debug=True)
            if f is not None and f.getExtension() == "sql":  # if the file is a sql file
                sql: dumpSqlFile = dumpSqlFile(path=DumpsPath + "/" + folder)
                if loadDumps != "all dumps" and loadDumps != sql.getNameDataBase():
                    continue
                else:
                    moveFile(sql.getPath(), pathLastDumpsFiles)
            else:
                print("File not found: " + folder)
                loadingLabel.config(text="File not found: " + folder)
                if success:
                    success = False
                    message = "Error: file not found\n" + \
                              "@space- " + folder + "\n"
                    code = 404
                else:
                    message += "@space- " + folder
    return Error(success=success, message=message, code=code)


def ShellRunner(loadingLabel: tk.Label = None, DockerFrame: DataManagerFrame = None, UserFrame: DataManagerFrame = None,
                PassWordFrame: DataManagerFrame = None, loadDumps: str = 'all dumps') -> Error:
    """
    dump all databases with a shell command
    :param loadingLabel: tk.Label, loading label
    :param DockerFrame: DataManagerFrame, docker frame
    :param UserFrame: DataManagerFrame, user frame
    :param PassWordFrame: DataManagerFrame, password frame
    :param loadDumps: str, load dumps
    :return: Error, error message
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

    user: str = get_user_name(UserFrame)
    password: str = get_password(PassWordFrame)

    # check if is a docker command and get the docker container if is necessary
    NameDockerContainer: str = get_docker_container(DockerFrame=DockerFrame)
    if NameDockerContainer is not None:  # if is a docker command
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

            # shell command to dump the database
            command: str = turnCommandeToExecutable(command=AddDumpsCommand,
                                                    user=user,
                                                    password=password,
                                                    dump=sql.getPath(),
                                                    NameDockerContainer=NameDockerContainer)

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


def GenerateDumps(loadingLabel: tk.Label = None, DockerFrame: DataManagerFrame = None,
                  UserFrame: DataManagerFrame = None, PassWordFrame: DataManagerFrame = None) -> Error:
    """
    generate a dump of the database
    :param loadingLabel: tk.Label, label to show the progress of the dump
    :param DockerFrame: DataManagerFrame, frame to show the docker container
    :param UserFrame: DataManagerFrame, frame to show the user
    :param PassWordFrame: DataManagerFrame, frame to show the password
    :return: Error, error message
    """
    success: bool = True
    message: str = "the dump is generated"
    code: int = 200

    CleanTerminal()

    CleanDumpsFolder(loadingLabel=loadingLabel)

    print("Dump started")

    user: str = get_user_name(UserFrame)
    password: str = get_password(PassWordFrame)

    # check if is a docker command and get the docker container if is necessary
    NameDockerContainer: str = get_docker_container(DockerFrame=DockerFrame)
    if NameDockerContainer is not None:  # if is a docker command
        print("Docker container: " + NameDockerContainer)

    numFolders: int = 0

    for db in listDatabasesWithoutSytemBase():
        numFolders += 1
        print("Generate dump: " + db)
        loadingLabel.config(text="Generate dump: " + db + " (" + str(numFolders) + "/" + str(
            len(listDatabasesWithoutSytemBase())) + ")")
        loadingLabel.update()

        # shell command to dump the database
        date: Date = getActualDate()
        strDate: str = "(" + date.getYearString() + "-" + date.getMonthString() + "-" + date.getDayString() + ")"
        command: str = turnCommandeToExecutable(command=GenerateDumpCommand,
                                                user=user,
                                                password=password,
                                                dump=DumpsPath + "/" + db + "_" + strDate + ".sql",
                                                NameDockerContainer=NameDockerContainer,
                                                db=db)

        print("Executing: " + command)

        try:
            os.system(command)
        except Exception as e:
            if success:
                success = False
                message = "Error to generate\n"
                code = 406
            message += "\n" + str(e)
            print("Error: " + str(e))
        else:
            print("Dump success")

        print("Executed: " + db + "\n")

    print("Dump finished")

    return Error(success=success, message=message, code=code)

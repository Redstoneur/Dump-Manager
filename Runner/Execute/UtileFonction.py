from Runner.DevFileManager import *
from Runner.Execute.ShellRunner import *
from Runner.LineFrame import *


def CleanDataInformation(errorLabel: tk.Label = None) -> None:
    """
    clean the terminal
    :return: None
    """
    # if the errorLabel is not None
    if errorLabel is not None:
        errorLabel.config(text=" ")

    CleanTerminal()


def AddDump(textfieldPath: tk.Text, listeDumps: tk.Listbox) -> None:
    """
    add a dump in the list of dumps
    :param textfieldPath: str, path of the dump
    :param listeDumps: list, list of dumps
    :return: None
    """
    path: str = textfieldPath.get("1.0", "end-1c")
    # if the path is not folder
    if not os.path.isdir(path):
        # if the path is a file
        if os.path.isfile(path):
            # if the file is a dump
            if isDumpSqlFile(path):
                # add the dump in the list of dumps
                moveFile(file=path, folder=DumpsPath)
                # reload the list of dumps
                Reload(listeDumps=listeDumps)
            else:
                print("Error: not a dump")
        else:
            print("Error: file not found")
    else:
        print("Error: folder not found")
    # clear the textfield
    textfieldPath.delete("1.0", "end-1c")
    textfieldPath.insert(tk.END, "C:/Users/alipio.simoes/Downloads/")


def Reload(listeDumps: tk.Listbox) -> None:
    """
    reload the list of dumps
    :param listeDumps: list, list of dumps
    :return: None
    """
    listeDumps.delete(0, tk.END)
    listOfDumps = ListOfDumps()
    for i in range(len(listOfDumps)):
        listeDumps.insert(i, listOfDumps[i])
    listeDumps.selection_set(0)


def information() -> bool:
    """
    print information about the program
    :return: bool, True if the program worked, False if not
    """

    # if have information
    if ApplicationInformation.haveData():
        # print information about the program
        print("\n" + ApplicationInformation.__str__() + "\n")
        return True

    else:  # if don't have information
        print("Error: information")
        return False


def Runner(loadingLabel: tk.Label = None, DockerFrame: DataManagerFrame = None, UserFrame: DataManagerFrame = None,
           loadDumps: str = 'all dumps', run: str = "nothing", graphique: bool = False) -> Error:
    """
    Run the program
    :param loadingLabel: tk.Label, label to display the error
    :param DockerFrame: DataManagerFrame, frame to display the docker container
    :param loadDumps: str, information or dump
    :param run: str, information or dump
    :param graphique: bool, if the program is run in graphique mode
    :return: Error, error object
    """
    CleanTerminal()

    error: Error
    start: WeekDay = getActualWeekDay()

    if information():  # if read information
        if run == "debugN1":  # if run in debug mode
            print("\nDebug mode N1")
            error = Error(success=True, message="Debug mode N1", code=2109)
        elif run == "shell":  # if run shell
            error = ShellRunner(loadingLabel=loadingLabel, DockerFrame=DockerFrame, UserFrame=UserFrame,
                                loadDumps=loadDumps)
        else:  # if run nothing
            error = Error(success=False, message="run not found", code=3)
    else:  # if not read information
        error = Error(success=False, message="Error: information", code=4)

    if not graphique:
        CalendarFileManager(titre="Get", description="Get the dumps",
                            start=start, error=error, graphique=False)
        LogFileManager(error=error)

    return error


def Run(errorLabel: tk.Label, loadingLabel: tk.Label, DockerFrame: DataManagerFrame = None,
        UserFrame: DataManagerFrame = None, loadDumps: str = 'all dumps', run: str = "nothing",
        isGet: bool = True, isClean: bool = False, isGenerate: bool = False) -> None:
    """
    display the error in the label
    :param errorLabel: label to display the error
    :param loadingLabel: label to display the loading
    :param DockerFrame: frame to display the docker container
    :param loadDumps: the dumps to load
    :param run: the command to run
    :param isGet: if the command is get
    :param isClean: if the command is clean
    :param isGenerate: if the command is generate
    :return: None
    """
    if isGet:
        isClean = False
        isGenerate = False
    elif isClean:
        isGet = False
        isGenerate = False
    elif isGenerate:
        isGet = False
        isClean = False
    else:
        isGet = False
        isClean = False
        isGenerate = False

    titre: str
    description: str

    if loadDumps != 'all dumps':
        loadDumps = loadDumps.split(' ')[0]
    start: WeekDay = getActualWeekDay()

    if isGet:
        error: Error = Runner(loadingLabel=loadingLabel, DockerFrame=DockerFrame, UserFrame=UserFrame,
                              loadDumps=loadDumps, run=run)
        titre = "Get"
        description = "Get the dumps"
    elif isClean:
        error: Error = CleanDumpsFolder(loadingLabel=loadingLabel)
        titre = "Clean"
        description = "Clean the dumps folder"
    elif isGenerate:
        error: Error = GenerateDumps(loadingLabel=loadingLabel, DockerFrame=DockerFrame, UserFrame=UserFrame, )
        titre = "Generate"
        description = "Generate the dumps"
    else:
        error: Error = Error(success=False, message="Nothing to run", code=5)
        titre = "Nothing"
        description = "Nothing to run"

    calendar: ErrorCalendar = CreateCalendar(titre=titre, description=description,
                                             start=start, error=error, graphique=True)
    loadingLabel.config(text=" ")
    loadingLabel.update()
    errorLabel.config(text=calendar.__str__())
    errorLabel.update()

    # create a file with a Calendar of the last dump
    CalendarFileManager(titre=titre, description=description,
                        start=start, error=error, graphique=False)
    # create a file log with the error
    LogFileManager(error=error)

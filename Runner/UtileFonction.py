import tkinter as tk
from Utilities import *
from Runner.DevFileManager.ApplicationInformation import *
from Runner.ShellRunner import DumpsPath, ListOfDumps, isDumpSqlFile, DatabaseInfo, get_default_docker_container

ApplicationInformation: ApplicationInformation = ApplicationInformation("./Data/package.json")
my_os: str = plt.system()


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


def textfieldDockerContainerLocker(textfieldDockerContainer: tk.Text,
                                   varCheckboxDockercontainer: tk.BooleanVar) -> None:
    """
    lock or unlock the textfieldDockerContainer
    :param textfieldDockerContainer: tk.Text, textfieldDockerContainer
    :param varCheckboxDockercontainer: tk.BooleanVar, varCheckboxDockercontainer
    :return: None
    """
    if varCheckboxDockercontainer.get():
        textfieldDockerContainer.config(state="disabled")
    else:
        textfieldDockerContainer.config(state="normal")


def textfieldDockerContainerToDefault(textfieldDockerContainer: tk.Text) -> None:
    """
    set the textfieldDockerContainer to default
    :param textfieldDockerContainer: tk.Text, textfieldDockerContainer
    :return: None
    """
    textfieldDockerContainer.delete("1.0", "end-1c")
    textfieldDockerContainer.insert("1.0", get_default_docker_container())


def textfieldDockerContainerToDefaultWithCheckbox(textfieldDockerContainer: tk.Text,
                                                  varCheckboxDockercontainer: tk.BooleanVar) -> None:
    """
    set the textfieldDockerContainer to default
    :param textfieldDockerContainer: tk.Text, textfieldDockerContainer
    :return: None
    """
    if varCheckboxDockercontainer.get():
        textfieldDockerContainer.config(state="normal")
        textfieldDockerContainerToDefault(textfieldDockerContainer=textfieldDockerContainer)
        textfieldDockerContainer.config(state="disabled")
    else:
        textfieldDockerContainerToDefault(textfieldDockerContainer=textfieldDockerContainer)


def AboutDB(txt: str) -> str:
    """
    get the information of the database
    :param txt: str, text of the database
    :return: str | None | dict, information of the database
    """
    if txt == "host":
        host: str = str(DatabaseInfo.get("host"))
        if host is not None or host != "":
            return host
        else:
            return "None"
    elif txt == "port":
        port: str = str(DatabaseInfo.get("port"))
        if port is not None or port != "":
            return port
        else:
            return "None"
    elif txt == "user":
        user: str = str(DatabaseInfo.get("user"))
        if user is not None or user != "":
            return user
        else:
            return "None"
    elif txt == "path-dumps":
        path_dumps: str = DumpsPath
        if path_dumps is not None or path_dumps != "":
            return path_dumps
        else:
            return "None"
    elif txt == "doker_container":
        doker_container: str = str(DatabaseInfo.get("doker_container"))
        if doker_container is not None or doker_container != "":
            return doker_container
        else:
            return "None"
    elif txt == "script-dumps":
        script_dumps: str = str(DatabaseInfo.get("script-dumps"))
        if script_dumps is not None or script_dumps != "":
            return script_dumps
        else:
            return "None"
    else:
        return "Error: information"


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

import tkinter as tk
import platform as plt
from Utile import *
from Runner.DevFileManager.ApplicationInformation import *
from Runner.ShellRunner import DumpsPath, ListOfDumps, isDumpSqlFile

ApplicationInformation: ApplicationInformation = ApplicationInformation("./Data/package.json")
my_os: str = plt.system()


def CleanTerminal() -> None:
    """
    clean the terminal
    :return: None
    """
    if my_os == "Windows":
        os.system("cls")
    else:
        os.system("clear")


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
import tkinter as tk
from Runner.DevFileManager import *
from Runner.ShellRunner import *
from Runner.DbRunner import *

ApplicationInformation: ApplicationInformation = ApplicationInformation("./Data/package.json")


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


def fenetre(run: str = "nothing") -> Error:
    """
    create a window
    :param run: str, information or dump
    :return: None
    """
    window: tk.Tk = tk.Tk()

    labelTitre: tk.Label
    labelTitreSubligne: tk.Label
    ComboboxDumps: tk.Listbox
    loadingLabel: tk.Label
    errorLabel: tk.Label
    RunButton: tk.Button
    ReloadButton: tk.Button
    error: Error

    longueur: int = 500
    hauteur: int = 500

    grid_rowconfigure_Max: int = 6
    grid_columnconfigure_Max: int = 4

    try:
        window.title(ApplicationInformation.name + " " + ApplicationInformation.version)
        window.geometry(str(longueur) + "x" + str(hauteur))

        for i in range(grid_rowconfigure_Max):
            window.grid_rowconfigure(i, weight=1)

        for i in range(grid_columnconfigure_Max):
            window.grid_columnconfigure(i, weight=1)

        # label titre
        labelTitre = tk.Label(window, text=ApplicationInformation.name)
        labelTitre.config(font=("Courier", 20))
        labelTitre.grid(row=0, column=0, columnspan=grid_columnconfigure_Max, sticky="nsew")

        # label subtitle
        labelTitreSubligne = tk.Label(window, text=ApplicationInformation.version)
        labelTitreSubligne.config(font=("Courier", 10))
        labelTitreSubligne.grid(row=1, column=0, columnspan=grid_columnconfigure_Max, sticky="nsew")

        # Select List
        ComboboxDumps = tk.Listbox(window)
        Reload(listeDumps=ComboboxDumps)
        ComboboxDumps.grid(row=2, column=0, columnspan=grid_columnconfigure_Max, sticky="nsew")

        # create a button to run the program
        RunButton = tk.Button(window, text="Run",
                              command=lambda: Run(errorLabel=errorLabel, loadingLabel=loadingLabel,
                                                  loadDumps=ComboboxDumps.get(ComboboxDumps.curselection()), run=run))
        RunButton.grid(row=3, column=0, columnspan=int(grid_columnconfigure_Max / 2), sticky="nsew")

        # create a button to reload the list of dumps
        ReloadButton = tk.Button(window, text="Reload", command=lambda: Reload(listeDumps=ComboboxDumps))
        ReloadButton.grid(row=3, column=int(grid_columnconfigure_Max / 2), columnspan=int(grid_columnconfigure_Max / 2),
                          sticky="nsew")

        # relative information label
        loadingLabel = tk.Label(window, text=" ", justify=tk.CENTER)
        loadingLabel.grid(row=4, column=0, columnspan=grid_columnconfigure_Max, sticky="nsew")

        # create a label to display the error
        errorLabel = tk.Label(window, text="", justify=tk.LEFT, anchor=tk.W)
        errorLabel.grid(row=5, column=0, columnspan=grid_columnconfigure_Max, sticky="nsew")

        window.mainloop()
    except Exception as e:
        print(e)
        return Error(success=False, message=str(e), code=5)
    else:
        return Error(success=True, message="Mode graphique was successfully run", code=200)


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


def Run(errorLabel: tk.Label, loadingLabel: tk.Label, loadDumps: str = 'all dumps', run: str = "nothing") -> None:
    """
    display the error in the label
    :param run: str, information or dump
    :param errorLabel: tk.Label, label to display the error
    :return: None
    """
    start: WeekDay = getActualWeekDay()
    error: Error = Runner(loadingLabel=loadingLabel, loadDumps=loadDumps, run=run)
    calendar: ErrorCalendar = CreateCalendar(start=start, error=error, graphique=True)
    loadingLabel.config(text=" ")
    loadingLabel.update()
    errorLabel.config(text=calendar.__str__())
    errorLabel.update()


def Runner(loadingLabel: tk.Label=None, loadDumps: str = 'all dumps', run: str = "nothing", graphique: bool = False) -> Error:
    """
    Run the program
    :param run: str, information or dump
    :param graphique: bool, if the program is run in graphique mode
    :return: Error, error object
    """
    error: Error
    start: WeekDay = getActualWeekDay()

    if graphique:
        error = fenetre(run=run)
    else:
        if information():  # if read information
            if run == "debugN1":  # if run in debug mode
                print("\nDebug mode N1")
                error = Error(success=True, message="Debug mode N1", code=2109)
            if run == "shell":  # if run shell
                error = ShellRunner(loadingLabel=loadingLabel, loadDumps=loadDumps)
            else:  # if run nothing
                error = Error(success=False, message="run not found", code=3)
        else:  # if not read information
            error = Error(success=False, message="Error: information", code=4)

        # create a file with a Calendar of the last dump
        CalendarFileManager(start=start, error=error, graphique=graphique)
        # create a file log with the error
        LogFileManager(error=error)

    return error

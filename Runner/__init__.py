from Runner.DevFileManager import *
from Runner.ShellRunner import *
from Runner.UtileFonction import *


# from Runner.DbRunner import *


def fenetre(run: str = "nothing") -> Error:
    """
    create a window
    :param run: str, information or dump
    :return: None
    """
    window: tk.Tk = tk.Tk()

    labelTitre: tk.Label
    labelTitreSubligne: tk.Label
    loadingLabel: tk.Label
    errorLabel: tk.Label
    LabelAddDump: tk.Label

    textfieldPath: tk.Text

    RunButton: tk.Button
    ReloadButton: tk.Button
    cleanTerminalButton: tk.Button
    useTextfieldButton: tk.Button

    ComboboxDumps: tk.Listbox

    error: Error

    longueur: int = 500
    hauteur: int = 500

    grid_rowconfigure_Max: int = 8
    grid_columnconfigure_Max: int = 3

    try:
        window.title(ApplicationInformation.get_name() + " " + ApplicationInformation.get_version())
        window.geometry(str(longueur) + "x" + str(hauteur))

        for i in range(grid_rowconfigure_Max):
            window.grid_rowconfigure(i, weight=1)

        for i in range(grid_columnconfigure_Max):
            window.grid_columnconfigure(i, weight=1)

        # position
        row: int = 0

        # label titre
        labelTitre = tk.Label(window, text=ApplicationInformation.get_name())
        labelTitre.config(font=("Courier", 20))
        labelTitre.grid(row=row, column=0, columnspan=grid_columnconfigure_Max, sticky="nsew")

        # position
        row += 1

        # label subtitle
        labelTitreSubligne = tk.Label(window, text=ApplicationInformation.get_version())
        labelTitreSubligne.config(font=("Courier", 10))
        labelTitreSubligne.grid(row=row, column=0, columnspan=grid_columnconfigure_Max, sticky="nsew")

        # position
        row += 1

        # label add dump
        LabelAddDump = tk.Label(window, text="Add dump:")
        LabelAddDump.grid(row=row, column=0, sticky="we")

        # path textfield
        textfieldPath = tk.Text(window, height=1, width=30)
        textfieldPath.insert(tk.END, "C:/Users/alipio.simoes/Downloads/")
        textfieldPath.grid(row=row, column=1, sticky="we")

        # use textfield button
        useTextfieldButton = tk.Button(window, text="Use",
                                       command=lambda: AddDump(textfieldPath=textfieldPath, listeDumps=ComboboxDumps))
        useTextfieldButton.grid(row=row, column=2, sticky="we")

        # position
        row += 1

        # Select List
        ComboboxDumps = tk.Listbox(window, justify="center")
        Reload(listeDumps=ComboboxDumps)
        ComboboxDumps.grid(row=row, column=0, columnspan=grid_columnconfigure_Max, sticky="nsew")

        # position
        row += 1

        # create a button to run the program
        RunButton = tk.Button(window, text="Run",
                              command=lambda: Run(errorLabel=errorLabel, loadingLabel=loadingLabel,
                                                  loadDumps=ComboboxDumps.get(ComboboxDumps.curselection()), run=run))
        RunButton.grid(row=row, column=0, sticky="nsew")

        # create a button to reload the list of dumps
        ReloadButton = tk.Button(window, text="Reload", command=lambda: Reload(listeDumps=ComboboxDumps))
        ReloadButton.grid(row=row, column=1, sticky="nsew")

        # create a button to clean the terminal
        cleanTerminalButton = tk.Button(window, text="Clean Terminal", command=lambda: CleanTerminal())
        cleanTerminalButton.grid(row=row, column=2, sticky="nsew")

        # position
        row += 1

        # relative information label
        loadingLabel = tk.Label(window, text=" ", justify=tk.CENTER)
        loadingLabel.grid(row=row, column=0, columnspan=grid_columnconfigure_Max, sticky="nsew")

        # position
        row += 1

        # create a label to display the error
        errorLabel = tk.Label(window, text="", justify=tk.LEFT, anchor=tk.W)
        errorLabel.grid(row=row, column=0, columnspan=grid_columnconfigure_Max, sticky="nsew")

        # position
        row += 1

        # label Author
        labelAuthor = tk.Label(window, text=ApplicationInformation.get_author())
        labelAuthor.config(font=("Arial", 7))
        labelAuthor.grid(row=row, column=0, sticky="sw")

        # label Copyright
        labelCopyright = tk.Label(window, text=ApplicationInformation.get_email())
        labelCopyright.config(font=("Arial", 7))
        labelCopyright.grid(row=row, column=1, sticky="s")

        # label version
        labelVersion = tk.Label(window, text="v" + ApplicationInformation.get_version())
        labelVersion.config(font=("Arial", 7))
        labelVersion.grid(row=row, column=grid_columnconfigure_Max - 1, sticky="se")

        window.mainloop()
    except Exception as e:
        print(e)
        return Error(success=False, message=str(e), code=5)
    else:
        return Error(success=True, message="Mode graphique was successfully run", code=200)


def Run(errorLabel: tk.Label, loadingLabel: tk.Label, loadDumps: str = 'all dumps', run: str = "nothing") -> None:
    """
    display the error in the label
    :param errorLabel: tk.Label, label to display the error
    :param loadingLabel: tk.Label, label to display the loading
    :param loadDumps: str, dump to load
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


def Runner(loadingLabel: tk.Label = None, loadDumps: str = 'all dumps', run: str = "nothing",
           graphique: bool = False) -> Error:
    """
    Run the program
    :param loadingLabel: tk.Label, label to display the error
    :param loadDumps: str, information or dump
    :param run: str, information or dump
    :param graphique: bool, if the program is run in graphique mode
    :return: Error, error object
    """
    CleanTerminal()

    error: Error
    start: WeekDay = getActualWeekDay()

    if graphique:
        error = fenetre(run=run)
    else:
        if information():  # if read information
            if run == "debugN1":  # if run in debug mode
                print("\nDebug mode N1")
                error = Error(success=True, message="Debug mode N1", code=2109)
            elif run == "shell":  # if run shell
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

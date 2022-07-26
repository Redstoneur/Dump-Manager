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
    # create the window
    window: tk.Tk = tk.Tk()

    # create the label
    labelTitre: tk.Label
    labelTitreSubligne: tk.Label
    loadingLabel: tk.Label
    errorLabel: tk.Label
    LabelAddDump: tk.Label
    LabelDockerContainer: tk.Label

    # create the textfield
    textfieldPathAddDump: tk.Text
    textfieldDockerContainer: tk.Text

    # create the button
    RunButton: tk.Button
    ReloadButton: tk.Button
    cleanTerminalButton: tk.Button
    useTextfieldPathAddDumpButton: tk.Button

    # create the listbox
    ComboboxDumps: tk.Listbox

    # create the checkbutton
    checkboxDockercontainer: tk.Checkbutton

    # create the boolean variable
    varCheckboxDockercontainer: tk.BooleanVar

    # create the menu
    menuButton: tk.Menu
    menuUtile: tk.Menu
    listSubMenuUtile: list[tk.Menu]
    menuInfoDb: tk.Menu
    listSubMenuInfoDb: list[tk.Menu]
    menuAbout: tk.Menu
    listSubMenuAbout: list[tk.Menu]

    # create the error object
    error: Error

    # define the size of the window
    longueur: int = 500
    hauteur: int = 500

    # define the size of the grid
    grid_rowconfigure_Max: int = 8
    grid_columnconfigure_Max: int = 3

    # add one row to the grid if the command is a docker command
    if isDockerCommand(shellStartCommand):
        grid_rowconfigure_Max += 1

    try:
        # define the title of the window
        window.title(ApplicationInformation.get_name() + " " + ApplicationInformation.get_version())
        # define the size of the window
        window.geometry(str(longueur) + "x" + str(hauteur))

        # create the menu bar
        menuButton = tk.Menu(window)

        # menu utile
        menuUtile = tk.Menu(menuButton)
        menuUtile.add_command(label="Run", command=lambda: Run(errorLabel=errorLabel, loadingLabel=loadingLabel,
                                                               textfieldDockerContainer=textfieldDockerContainer,
                                                               loadDumps=ComboboxDumps.get(
                                                                   ComboboxDumps.curselection()), run=run))
        # menuUtile.add_command(label="Use textfield path add dump", command=lambda: useTextfieldPathAddDump())
        menuUtile.add_command(label="Default docker container",
                              command=lambda: textfieldDockerContainerToDefaultWithCheckbox(
                                  textfieldDockerContainer=textfieldDockerContainer,
                                  varCheckboxDockercontainer=varCheckboxDockercontainer))
        menuUtile.add_command(label="Reload", command=lambda: Reload(listeDumps=ComboboxDumps))
        menuUtile.add_command(label="Clean terminal", command=lambda: CleanDataInformation(errorLabel=errorLabel))
        menuUtile.add_command(label="Clean Dumps folder", command=lambda: print(CleanDumpsFolder().__str__() + "\n"))
        menuUtile.add_command(label="Quit", command=lambda: window.destroy())
        menuUtile.add_command(label="Exit", command=lambda: exit())

        menuButton.add_cascade(label="Utile", menu=menuUtile)

        # add the menu Cascade menuInfoDb
        menuInfoDb = tk.Menu(menuButton, tearoff=0)

        listSubMenuInfoDb: list[tk.Menu] = [tk.Menu(menuInfoDb, tearoff=0) for i in range(3)]

        listSubMenuInfoDb[0].add_command(label="Host : " + AboutDB("host"))
        listSubMenuInfoDb[0].add_command(label="Port : " + AboutDB("port"))
        listSubMenuInfoDb[0].add_command(label="user : " + AboutDB("user"))
        menuInfoDb.add_cascade(label="Database", menu=listSubMenuInfoDb[0])

        listSubMenuInfoDb[1].add_command(label="Path of dump : " + AboutDB("path-dumps"))
        menuInfoDb.add_cascade(label="Dump", menu=listSubMenuInfoDb[1])

        listSubMenuInfoDb[2].add_command(label="Script for execute dumps : " + AboutDB("script-dumps"))
        if isDockerCommand(shellStartCommand):
            listSubMenuInfoDb[2].add_command(label="Docker container by default : " + AboutDB("doker_container"))
        menuInfoDb.add_cascade(label="Script", menu=listSubMenuInfoDb[2])

        menuButton.add_cascade(label="Info DB", menu=menuInfoDb)

        # add the menu Cascade menuAbout
        menuAbout = tk.Menu(menuButton, tearoff=0)

        listSubMenuAbout: list[tk.Menu] = [tk.Menu(menuAbout, tearoff=0) for i in range(2)]

        listSubMenuAbout[0].add_command(label="Name : " + ApplicationInformation.name)
        listSubMenuAbout[0].add_command(label="Version : " + ApplicationInformation.version)
        listSubMenuAbout[0].add_command(label="License : " + str(ApplicationInformation.get("license")))
        menuAbout.add_cascade(label="About", menu=listSubMenuAbout[0])

        listSubMenuAbout[1].add_command(label="Author : " + ApplicationInformation.author_first_name +
                                              " " + ApplicationInformation.author_last_name)
        listSubMenuAbout[1].add_command(label="Email : " + ApplicationInformation.email)
        listSubMenuAbout[1].add_command(label="Website : " + str(ApplicationInformation.get("website")))
        menuAbout.add_cascade(label="Contact", menu=listSubMenuAbout[1])

        menuButton.add_cascade(label="About", menu=menuAbout)

        window.config(menu=menuButton)

        # create the grid for the window
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

        if isDockerCommand(shellStartCommand):
            # position
            row += 1

            # label docker container
            LabelDockerContainer = tk.Label(window, text="Docker container:")
            LabelDockerContainer.grid(row=row, column=0, sticky="we")

            # textfield docker container
            textfieldDockerContainer = tk.Text(window, height=1, width=20)
            textfieldDockerContainer.insert(tk.END, get_default_docker_container())
            textfieldDockerContainer.grid(row=row, column=1, sticky="we")

            # checkbox docker container
            varCheckboxDockercontainer = tk.BooleanVar()
            checkboxDockercontainer = tk.Checkbutton(window, text="Use docker container",
                                                     variable=varCheckboxDockercontainer, onvalue=True, offvalue=False,
                                                     command=lambda: textfieldDockerContainerLocker(
                                                         textfieldDockerContainer=textfieldDockerContainer,
                                                         varCheckboxDockercontainer=varCheckboxDockercontainer))
            checkboxDockercontainer.select()
            textfieldDockerContainerLocker(textfieldDockerContainer=textfieldDockerContainer,
                                           varCheckboxDockercontainer=varCheckboxDockercontainer)
            checkboxDockercontainer.grid(row=row, column=2, sticky="we")

        else:
            # noinspection PyTypeChecker
            textfieldDockerContainer = None

        # position
        row += 1

        # label add dump
        LabelAddDump = tk.Label(window, text="Add dump:")
        LabelAddDump.grid(row=row, column=0, sticky="we")

        # path textfield
        textfieldPathAddDump = tk.Text(window, height=1, width=30)
        textfieldPathAddDump.insert(tk.END, "C:/Users/alipio.simoes/Downloads/")
        textfieldPathAddDump.grid(row=row, column=1, sticky="we")

        # use textfield button
        useTextfieldPathAddDumpButton = tk.Button(window, text="Use",
                                                  command=lambda: AddDump(textfieldPath=textfieldPathAddDump,
                                                                          listeDumps=ComboboxDumps))
        useTextfieldPathAddDumpButton.grid(row=row, column=2, sticky="we")

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
                                                  textfieldDockerContainer=textfieldDockerContainer,
                                                  loadDumps=ComboboxDumps.get(ComboboxDumps.curselection()), run=run))
        RunButton.grid(row=row, column=0, sticky="nsew")

        # create a button to reload the list of dumps
        ReloadButton = tk.Button(window, text="Reload", command=lambda: Reload(listeDumps=ComboboxDumps))
        ReloadButton.grid(row=row, column=1, sticky="nsew")

        # create a button to clean the terminal
        cleanTerminalButton = tk.Button(window, text="Clean Terminal",
                                        command=lambda: CleanDataInformation(errorLabel=errorLabel))
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


def Run(errorLabel: tk.Label, loadingLabel: tk.Label, textfieldDockerContainer: tk.Text = None,
        loadDumps: str = 'all dumps', run: str = "nothing") -> None:
    """
    display the error in the label
    :param errorLabel: tk.Label, label to display the error
    :param loadingLabel: tk.Label, label to display the loading
    :param loadDumps: str, dump to load
    :param run: str, information or dump
    :param errorLabel: tk.Label, label to display the error
    :return: None
    """
    if loadDumps != 'all dumps':
        loadDumps = loadDumps.split(' ')[0]
    start: WeekDay = getActualWeekDay()
    error: Error = Runner(loadingLabel=loadingLabel, textfieldDockerContainer=textfieldDockerContainer,
                          loadDumps=loadDumps, run=run)
    calendar: ErrorCalendar = CreateCalendar(start=start, error=error, graphique=True)
    loadingLabel.config(text=" ")
    loadingLabel.update()
    errorLabel.config(text=calendar.__str__())
    errorLabel.update()


def Runner(loadingLabel: tk.Label = None, textfieldDockerContainer: tk.Text = None, loadDumps: str = 'all dumps',
           run: str = "nothing",
           graphique: bool = False) -> Error:
    """
    Run the program
    :param loadingLabel: tk.Label, label to display the error
    :param textfieldDockerContainer: tk.Text, textfield to display the docker container
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
                error = ShellRunner(loadingLabel=loadingLabel, textfieldDockerContainer=textfieldDockerContainer,
                                    loadDumps=loadDumps)
            else:  # if run nothing
                error = Error(success=False, message="run not found", code=3)
        else:  # if not read information
            error = Error(success=False, message="Error: information", code=4)

        # create a file with a Calendar of the last dump
        CalendarFileManager(start=start, error=error, graphique=graphique)
        # create a file log with the error
        LogFileManager(error=error)

    return error

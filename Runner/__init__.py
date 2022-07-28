from Runner.DevFileManager import *
from Runner.ShellRunner import *
from Runner.UtileFonction import *
from Runner.BareMenu import *


def start(run: str = "nothing", graphique: bool = False) -> Error:
    """
    start the program
    :param run: str, information or dump
    :param graphique: bool, if the program is run in graphique mode
    :return: None
    """
    if graphique:
        return fenetre(run=run)
    else:
        return Runner(run=run, graphique=graphique)


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
    menu: BareMenu

    # create the error object
    error: Error

    # define the size of the window
    longueur: int = 600
    hauteur: int = 600

    # define the size of the grid
    grid_rowconfigure_Max: int = 8
    grid_columnconfigure_Max: int = 3

    # add one row to the grid if the command is a docker command
    if isDockerCommand(AddDumpsCommand):
        grid_rowconfigure_Max += 1

    try:
        # define the title of the window
        window.title(ApplicationInformation.get_name() + " " + ApplicationInformation.get_version())
        # define the size of the window
        window.geometry(str(longueur) + "x" + str(hauteur))

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

        if isDockerCommand(AddDumpsCommand):
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
            # noinspection PyTypeChecker
            varCheckboxDockercontainer = None

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

        # create the menu bar
        menu = BareMenu(master=window, errorLabel=errorLabel, loadingLabel=loadingLabel,
                        textfieldDockerContainer=textfieldDockerContainer, ComboboxDumps=ComboboxDumps,
                        varCheckboxDockercontainer=varCheckboxDockercontainer, run=run)
        window.config(menu=menu)

        window.mainloop()
    except Exception as e:
        print(e)
        return Error(success=False, message=str(e), code=5)
    else:
        return Error(success=True, message="Mode graphique was successfully run", code=200)

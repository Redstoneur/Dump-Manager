from Runner.LineFrame import *
from Runner.BareMenu import *


#####################################################################################################################
############################# Class Window ##########################################################################
#####################################################################################################################

class Window(tk.Tk):
    """
    create a window
    @description: create a window
    @author: Redstoneur
    @version: 1.0
    """

    # label
    labelTitre: tk.Label
    labelTitreSubligne: tk.Label
    loadingLabel: tk.Label
    errorLabel: tk.Label
    LabelAddDump: tk.Label
    LabelDockerContainer: tk.Label

    # textfield
    textfieldPathAddDump: tk.Text

    # button
    RunButton: tk.Button
    ReloadButton: tk.Button
    cleanTerminalButton: tk.Button
    useTextfieldPathAddDumpButton: tk.Button

    # listbox
    ComboboxDumps: tk.Listbox

    # menu
    menu: BareMenu

    # Frame
    UserFrame: DataManagerFrame
    PassWordFrame: DataManagerFrame
    DockerFrame: DataManagerFrame
    endFrame: EndFrame

    def __init__(self, run: str = "nothing", heightResizable: bool = False, widthResizable: bool = False,
                 height: int = 600, width: int = 600) -> None:
        """
        create a window
        @description: function to create a window
        :param run: str, information or dump
        :param height: int, height of the window
        :param width: int, width of the window
        :return: None
        """
        super().__init__()

        # set the title of the window
        self.title(ApplicationInformation.get_name() + " " + ApplicationInformation.get_version())
        # set the size of the window
        self.geometry(f"{width}x{height}")
        # set resizable to false
        self.resizable(widthResizable, heightResizable)

        # set run variable
        self.run = run

        # define max column
        self.grid_columnconfigure_Max = 3

        for i in range(self.grid_columnconfigure_Max):
            self.grid_columnconfigure(i, weight=1)

        self.create_widgets()
        self.mainloop()

    def create_widgets(self):
        """
        create the widgets
        @description: function to create the widgets
        :return: None
        """
        # position
        row: int = 0
        self.grid_rowconfigure(row, weight=1)

        # label titre
        self.labelTitre = tk.Label(self, text=ApplicationInformation.get_name())
        self.labelTitre.config(font=("Courier", 20))
        self.labelTitre.grid(row=row, column=0, columnspan=self.grid_columnconfigure_Max, sticky="nsew")

        # position
        row += 1
        self.grid_rowconfigure(row, weight=1)

        # label subtitle
        self.labelTitreSubligne = tk.Label(self, text=ApplicationInformation.get_version())
        self.labelTitreSubligne.config(font=("Courier", 10))
        self.labelTitreSubligne.grid(row=row, column=0, columnspan=self.grid_columnconfigure_Max, sticky="nsew")

        # position
        row += 1
        self.grid_rowconfigure(row, weight=1)

        Userkey: str = "user"
        self.UserFrame = DataManagerFrame(master=self,
                                          grid_columnconfigure_Max=self.grid_columnconfigure_Max,
                                          textlabel=Userkey,
                                          defaultValueTextfield=str(DatabaseInfo.get(Userkey)),
                                          textCheckbox="Use value",
                                          defaultValueCheckbox=True)

        self.UserFrame.grid(row=row, column=0, columnspan=self.grid_columnconfigure_Max,
                            sticky="nsew")

        # position
        # row += 1
        # self.grid_rowconfigure(row, weight=1)
        #
        # PassWordkey: str = "user"
        # self.PassWordFrame = DataManagerFrame(master=self,
        #                                       grid_columnconfigure_Max=self.grid_columnconfigure_Max,
        #                                       textlabel=PassWordkey,
        #                                       defaultValueTextfield=str(DatabaseInfo.get(PassWordkey)),
        #                                       textCheckbox="Use value",
        #                                       defaultValueCheckbox=True,
        #                                       isPassword=True)
        #
        # self.PassWordFrame.grid(row=row, column=0, columnspan=self.grid_columnconfigure_Max,
        #                         sticky="nsew")

        if isDockerCommand(AddDumpsCommand):
            # position
            row += 1
            self.grid_rowconfigure(row, weight=1)

            Dockerkey: str = "doker_container"
            self.DockerFrame = DataManagerFrame(master=self,
                                                grid_columnconfigure_Max=self.grid_columnconfigure_Max,
                                                textlabel=Dockerkey,
                                                defaultValueTextfield=str(DatabaseInfo.get(Dockerkey)),
                                                textCheckbox="Use value",
                                                defaultValueCheckbox=True)

            self.DockerFrame.grid(row=row, column=0, columnspan=self.grid_columnconfigure_Max,
                                  sticky="nsew")

        else:
            # noinspection PyTypeChecker
            self.DockerFrame = None

        # position
        row += 1
        self.grid_rowconfigure(row, weight=1)

        # label add dump
        self.LabelAddDump = tk.Label(self, text="Add dump:")
        self.LabelAddDump.grid(row=row, column=0, sticky="we")

        # path textfield
        self.textfieldPathAddDump = tk.Text(self, height=1, width=30)
        self.textfieldPathAddDump.insert(tk.END, "C:/Users/alipio.simoes/Downloads/")
        self.textfieldPathAddDump.grid(row=row, column=1, sticky="we")

        # use textfield button
        self.useTextfieldPathAddDumpButton = tk.Button(self, text="Use",
                                                       command=lambda: AddDump(textfieldPath=self.textfieldPathAddDump,
                                                                               listeDumps=self.ComboboxDumps))
        self.useTextfieldPathAddDumpButton.grid(row=row, column=2, sticky="we")

        # position
        row += 1
        self.grid_rowconfigure(row, weight=1)

        # Select List
        self.ComboboxDumps = tk.Listbox(self, justify="center")
        Reload(listeDumps=self.ComboboxDumps)
        self.ComboboxDumps.grid(row=row, column=0, columnspan=self.grid_columnconfigure_Max, sticky="nsew")

        # position
        row += 1
        self.grid_rowconfigure(row, weight=1)

        # create a button to run the program
        self.RunButton = tk.Button(self, text="Run",
                                   command=lambda: Run(errorLabel=self.errorLabel, loadingLabel=self.loadingLabel,
                                                       DockerFrame=self.DockerFrame, UserFrame=self.UserFrame,
                                                       loadDumps=self.ComboboxDumps.get(
                                                           self.ComboboxDumps.curselection()), run=self.run))
        self.RunButton.grid(row=row, column=0, sticky="nsew")

        # create a button to reload the list of dumps
        self.ReloadButton = tk.Button(self, text="Reload", command=lambda: Reload(listeDumps=self.ComboboxDumps))
        self.ReloadButton.grid(row=row, column=1, sticky="nsew")

        # create a button to clean the terminal
        self.cleanTerminalButton = tk.Button(self, text="Clean Terminal",
                                             command=lambda: CleanDataInformation(errorLabel=self.errorLabel))
        self.cleanTerminalButton.grid(row=row, column=2, sticky="nsew")

        # position
        row += 1
        self.grid_rowconfigure(row, weight=1)

        # relative information label
        self.loadingLabel = tk.Label(self, text=" ", justify=tk.CENTER)
        self.loadingLabel.grid(row=row, column=0, columnspan=self.grid_columnconfigure_Max, sticky="nsew")

        # position
        row += 1
        self.grid_rowconfigure(row, weight=1)

        # create a label to display the error
        self.errorLabel = tk.Label(self, text="", justify=tk.LEFT, anchor=tk.W)
        self.errorLabel.grid(row=row, column=0, columnspan=self.grid_columnconfigure_Max, sticky="nsew")

        # position
        row += 1
        self.grid_rowconfigure(row, weight=1)

        # create the end Frame
        self.endFrame = EndFrame(self, self.grid_columnconfigure_Max)
        self.endFrame.grid(row=row, column=0, columnspan=self.grid_columnconfigure_Max, sticky="nsew")

        # create the menu bar
        self.menu = BareMenu(master=self, errorLabel=self.errorLabel, loadingLabel=self.loadingLabel,
                             DockerFrame=self.DockerFrame, UserFrame=self.UserFrame,
                             ComboboxDumps=self.ComboboxDumps, run=self.run)
        self.config(menu=self.menu)

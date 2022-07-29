from Runner.Execute.UtileFonction import *


#####################################################################################################################
############################# Class Bare Menu #######################################################################
#####################################################################################################################

class BareMenu(tk.Menu):
    """
    class of the menu
    @description: set the menu
    @author: Redstoneur
    @version: 1.0
    """

    menuUtile: tk.Menu
    menuInfoDb: tk.Menu
    listSubMenuInfoDb: list[tk.Menu]
    menuAbout: tk.Menu
    listSubMenuAbout: list[tk.Menu]

    def __init__(self, master: tk.Tk, errorLabel: tk.Label, loadingLabel: tk.Label,
                 DockerFrame: DataManagerFrame = None, UserFrame: DataManagerFrame = None,
                 PassWordFrame: DataManagerFrame = None,
                 ComboboxDumps: tk.Listbox = None, run: str = "nothing") -> None:
        """
        Start of the class
        @description: function to Start the class
        :param master: tk.Tk, main window
        :param errorLabel: tk.Label, label of error
        :param loadingLabel: tk.Label, label of loading
        :param DockerFrame: DataManagerFrame, frame of docker
        :param UserFrame: DataManagerFrame, frame of user
        :param PassWordFrame: DataManagerFrame, frame of password
        :param ComboboxDumps: tk.Listbox, combobox of dumps
        :param run: str, run command
        :return: None
        """
        super().__init__(master)
        self.master = master
        self.errorLabel = errorLabel
        self.loadingLabel = loadingLabel
        self.DockerFrame = DockerFrame
        self.UserFrame = UserFrame
        self.PassWordFrame = PassWordFrame
        self.ComboboxDumps = ComboboxDumps
        self.run = run
        self.create_menu()

    def create_menu(self) -> None:
        """
        create menu
        @description: function to create the menu
        :return: None
        """
        # add menu utile
        self.menuUtile = tk.Menu(self)
        self.create_menu_utile()
        self.add_cascade(label="Utile", menu=self.menuUtile)

        # add menu info db
        self.menuInfoDb = tk.Menu(self, tearoff=0)
        self.create_menu_info_db()
        self.add_cascade(label="Info DB", menu=self.menuInfoDb)

        # add menu about
        self.menuAbout = tk.Menu(self, tearoff=0)
        self.create_menu_about()
        self.add_cascade(label="About", menu=self.menuAbout)

    def create_menu_utile(self) -> None:
        """
        create menu utile
        @description: function to create the menu utile
        :return: None
        """
        self.menuUtile.add_command(label="Run",
                                   command=lambda: Run(errorLabel=self.errorLabel, loadingLabel=self.loadingLabel,
                                                       DockerFrame=self.DockerFrame, UserFrame=self.UserFrame,
                                                       PassWordFrame=self.PassWordFrame,
                                                       loadDumps=self.ComboboxDumps.get(
                                                           self.ComboboxDumps.curselection()), run=self.run))
        # menuUtile.add_command(label="Use textfield path add dump", command=lambda: useTextfieldPathAddDump())
        self.menuUtile.add_command(label="Default user", command=lambda: self.UserFrame.set_default())
        self.menuUtile.add_command(label="Default docker container",
                                   command=lambda: self.DockerFrame.set_default())
        self.menuUtile.add_command(label="Reload", command=lambda: Reload(listeDumps=self.ComboboxDumps))
        self.menuUtile.add_command(label="Clean terminal",
                                   command=lambda: CleanDataInformation(errorLabel=self.errorLabel))
        self.menuUtile.add_command(label="Clean Dumps folder",
                                   command=lambda: Run(errorLabel=self.errorLabel, loadingLabel=self.loadingLabel,
                                                       PassWordFrame=self.PassWordFrame,
                                                       isGet=False, isClean=True, isGenerate=False))
        self.menuUtile.add_command(label="Generate Dumps",
                                   command=lambda: Run(errorLabel=self.errorLabel, loadingLabel=self.loadingLabel,
                                                       DockerFrame=self.DockerFrame, UserFrame=self.UserFrame,
                                                       PassWordFrame=self.PassWordFrame,
                                                       isGet=False, isClean=False, isGenerate=True))
        self.menuUtile.add_command(label="Quit", command=lambda: self.master.destroy())
        self.menuUtile.add_command(label="Exit", command=lambda: exit())

    def create_menu_info_db(self) -> None:
        """
        create menu info db
        @description: function to create the menu info db
        :return: None
        """
        self.listSubMenuInfoDb: list[tk.Menu] = [tk.Menu(self.menuInfoDb, tearoff=0) for _ in range(3)]

        self.listSubMenuInfoDb[0].add_command(label="Host : " + self.AboutDB("host"))
        self.listSubMenuInfoDb[0].add_command(label="Port : " + self.AboutDB("port"))
        self.listSubMenuInfoDb[0].add_command(label="user : " + self.AboutDB("user"))
        self.menuInfoDb.add_cascade(label="Database", menu=self.listSubMenuInfoDb[0])

        self.listSubMenuInfoDb[1].add_command(label="Path of dump : " + self.AboutDB("path-dumps"))
        self.menuInfoDb.add_cascade(label="Dump", menu=self.listSubMenuInfoDb[1])

        for i in DatabaseInfo.get_keys():
            if "script" in i:
                self.listSubMenuInfoDb[2].add_command(label=i + " : " + self.AboutDB(i))
        if isDockerCommand(AddDumpsCommand):
            self.listSubMenuInfoDb[2].add_command(
                label="Docker container by default : " + self.AboutDB("doker_container"))
        self.menuInfoDb.add_cascade(label="Script", menu=self.listSubMenuInfoDb[2])

    def create_menu_about(self) -> None:
        """
        create menu about
        @description: function to create the menu about
        :return: None
        """
        self.listSubMenuAbout: list[tk.Menu] = [tk.Menu(self.menuAbout, tearoff=0) for _ in range(2)]

        self.listSubMenuAbout[0].add_command(label="Name : " + ApplicationInformation.name)
        self.listSubMenuAbout[0].add_command(label="Version : " + ApplicationInformation.version)
        self.listSubMenuAbout[0].add_command(label="License : " + str(ApplicationInformation.get("license")))
        self.menuAbout.add_cascade(label="About", menu=self.listSubMenuAbout[0])

        self.listSubMenuAbout[1].add_command(label="Author : " + ApplicationInformation.author_first_name +
                                                   " " + ApplicationInformation.author_last_name)
        self.listSubMenuAbout[1].add_command(label="Email : " + ApplicationInformation.email)
        self.listSubMenuAbout[1].add_command(label="Website : " + str(ApplicationInformation.get("website")))
        self.menuAbout.add_cascade(label="Contact", menu=self.listSubMenuAbout[1])

    @staticmethod
    def AboutDB(txt: str) -> str:
        """
        get the information of the database
        @description: function to get the information of the database
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
        elif txt == "script-dumps-generator":
            script_dumps_generator: str = str(DatabaseInfo.get("script-dumps-generator"))
            if script_dumps_generator is not None or script_dumps_generator != "":
                return script_dumps_generator
            else:
                return "None"
        else:
            return "Error: information"

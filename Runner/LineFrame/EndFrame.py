from Runner.LineFrame.LineFrame import *
from Runner.Execute.varShellRunner import ApplicationInformation


#####################################################################################################################
############################# Class EndFrame ########################################################################
#####################################################################################################################

class EndFrame(LineFrame):
    """
    Class to create the End Frame
    @description: class to create the end frame
    @author: Redstoneur
    @version: 1.0
    """

    def __init__(self, master: tk.Tk, grid_columnconfigure_Max: int) -> None:
        """
        init of the class
        @description: function to init the class
        :param master: tk.Tk, main window
        :return: None
        """
        super().__init__(master, grid_columnconfigure_Max)

        self.create_widgets()

    def create_widgets(self):
        """
        create widgets
        @description: function to create the widgets
        :return: None
        """
        # label Author
        labelAuthor = tk.Label(self, text=ApplicationInformation.get_author())
        labelAuthor.config(font=("Arial", 7))
        labelAuthor.grid(row=0, column=0, sticky="sw")

        # label Copyright
        labelCopyright = tk.Label(self, text=ApplicationInformation.get_email())
        labelCopyright.config(font=("Arial", 7))
        labelCopyright.grid(row=0, column=1, sticky="s")

        # label version
        labelVersion = tk.Label(self, text="v" + ApplicationInformation.get_version())
        labelVersion.config(font=("Arial", 7))
        labelVersion.grid(row=0, column=self.grid_columnconfigure_Max - 1, sticky="se")

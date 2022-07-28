from abc import *
import tkinter as tk


#####################################################################################################################
############################# Class Line Frame ######################################################################
#####################################################################################################################


class LineFrame(tk.Frame):
    """
    Class Line Frame
    @description: class to create a line frame
    @author: Redstoneur
    @version: 1.0
    """
    grid_columnconfigure_Max: int

    @abstractmethod
    def __init__(self, master: tk.Tk, grid_columnconfigure_Max: int) -> None:
        """
        init of the class
        @description: function to init the class
        :param master: tk.Tk, main window
        :return: None
        """
        super().__init__()
        self.master: tk.Tk = master
        self.grid_columnconfigure_Max: int = grid_columnconfigure_Max

        self.grid_rowconfigure(0, weight=1)

        for i in range(self.grid_columnconfigure_Max):
            self.grid_columnconfigure(i, weight=1)

        pass

    @abstractmethod
    def create_widgets(self):
        """
        create widgets
        @description: function to create the widgets
        :return: None
        """
        pass

from Runner.LineFrame.LineFrame import *


#####################################################################################################################
############################# Class Variable Manager Frame ##############################################################
#####################################################################################################################

class DataManagerFrame(LineFrame):
    """
    Class Variable Manager Frame
    @description: class to create the data manager frame
    @author: Redstoneur
    @version: 1.0
    """

    label: tk.Label
    textfield: tk.Entry
    booleanVar: tk.BooleanVar
    checkbox: tk.Checkbutton
    booleanVar_password: tk.BooleanVar
    checkbox_password: tk.Checkbutton

    def __init__(self, master: tk.Tk, grid_columnconfigure_Max: int,
                 textlabel: str, defaultValueTextfield: str, textCheckbox: str,
                 defaultValueCheckbox: bool = True, isPassword: bool = False) -> None:
        """
        Start of the class
        @description: function to Start the class
        :param master: tk.Tk, main window
        :return: None
        """
        super().__init__(master, grid_columnconfigure_Max)

        self.textlabel: str = textlabel
        self.defaultValueTextfield: str = defaultValueTextfield
        self.textCheckbox: str = textCheckbox
        self.defaultValueCheckbox: bool = defaultValueCheckbox
        self.isPassword: bool = isPassword

        self.create_widgets()

    def create_widgets(self):
        """
        create widgets
        @description: function to create the widgets
        :return: None
        """
        # label
        column: int = 0
        self.create_Label(column=column)

        column += 1
        self.create_textfield(column=column)

        # checkbox
        column += 1
        self.create_checkbox(column=column)

        # textfield
        if self.isPassword:
            column += 1
            self.create_checkbox_password(column=column)

    def create_Label(self, column: int, sticky: str = "we"):
        """
        create label
        @description: function to create the label
        :param column: int, column
        :param sticky: str, sticky
        :return: None
        """
        self.label = tk.Label(self, text=self.textlabel, height=1, width=10)
        self.label.grid(row=0, column=column, sticky=sticky)

    def create_textfield(self, column: int, sticky: str = "we"):
        """
        create textfield
        @description: function to create the textfield
        :param column: int, column
        :param sticky: str, sticky
        :return: None
        """
        if self.isPassword:
            self.textfield = tk.Entry(self, show="*", width=20)
        else:
            self.textfield = tk.Entry(self, show="", width=20)
        self.textfield.insert(tk.END, self.get_default())
        self.textfield.grid(row=0, column=column, sticky=sticky)

    def create_checkbox(self, column: int, sticky: str = "we"):
        """
        create checkbox
        @description: function to create the checkbox
        :param column: int, column
        :param sticky: str, sticky
        :return: None
        """
        self.booleanVar = tk.BooleanVar()
        self.checkbox = tk.Checkbutton(self, text=self.textCheckbox, variable=self.booleanVar, onvalue=True,
                                       offvalue=False, command=lambda: self.textfieldLocker())
        if self.defaultValueCheckbox:
            self.checkbox.select()
        else:
            self.checkbox.deselect()
        self.textfieldLocker()
        self.checkbox.grid(row=0, column=column, sticky=sticky)

    def create_checkbox_password(self, column: int, sticky: str = "we"):
        """
        create checkbox password
        @description: function to create the checkbox password
        :param column: int, column
        :param sticky: str, sticky
        :return: None
        """
        self.booleanVar_password = tk.BooleanVar()
        self.checkbox_password = tk.Checkbutton(self, text="show", variable=self.booleanVar_password, onvalue=True,
                                                height=1,
                                                offvalue=False, command=lambda: self.set_show_password())
        if self.defaultValueCheckbox:
            self.checkbox_password.select()
        else:
            self.checkbox_password.deselect()
        self.set_show_password()
        self.checkbox_password.grid(row=0, column=column, sticky=sticky)

    def get_textfield_value(self):
        """
        get textfield value
        @description: function to get the textfield value
        :return: str
        """
        return self.textfield.get().replace("\n", "")

    def get_default(self):
        """
        get default value
        @description: function to get the default value
        :return: str
        """
        return self.defaultValueTextfield

    def textfieldLocker(self):
        """
        textfield locker
        @description: function to lock the textfield
        :return: None
        """
        if self.booleanVar.get():
            self.textfield.config(state="disabled")
        else:
            self.textfield.config(state="normal")

    def set_default(self, value: str = None):
        """
        set default value
        @description: function to set the default value
        :param value: str, value
        :return: None
        """
        if self.booleanVar.get():
            self.textfield.config(state="normal")

        self.textfield.delete("1.0", tk.END)
        if value is not None:
            self.defaultValueTextfield = value
        self.textfield.insert(tk.END, self.defaultValueTextfield)

        if self.booleanVar.get():
            self.textfield.config(state="disabled")

    def set_show_password(self):
        """
        set show password
        @description: function to set the show password
        :return: None
        """
        if self.isPassword:
            if self.booleanVar_password.get():
                self.textfield.config(show="*")
            else:
                self.textfield.config(show="")

def LibrairyUtilities_fr():
    try:
        import Utilities
    except ImportError:
        print("La librairie 'Utilities' n'est pas présente sur le système")
        print("Veuillez l'installer la librairie 'Utilities'")
        print("You can")
        exit()
    else:
        print("La librairie 'Utilities' est présente sur le système")
        print("")


def LibrairyUtilities_en():
    try:
        import Utilities
    except ImportError:
        print("The library 'Utilities' is not present on the system")
        print("Please install the library 'Utilities'")
        print("You can")
        exit()
    else:
        print("The library 'Utilities' is present on the system")
        print("")

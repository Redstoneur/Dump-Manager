from Utile import *
from Runner.ShellRunner import *

ApplicationInformation: JsonFile = JsonFile("./Data/package.json")


def information() -> bool:
    """
    print information about the program
    :return: bool, True if the program worked, False if not
    """

    # noinspection PyTypeChecker
    name: str = ApplicationInformation.get("name")
    # noinspection PyTypeChecker
    version: str = ApplicationInformation.get("version")
    # noinspection PyTypeChecker
    description: str = ApplicationInformation.get("description-en")
    # noinspection PyTypeChecker
    author_first_name: str = ApplicationInformation.get("author")["firstName"]
    # noinspection PyTypeChecker
    author_last_name: str = ApplicationInformation.get("author")["lastName"]

    # if have information
    if name is not None \
            and version is not None \
            and description is not None \
            and author_first_name is not None \
            and author_last_name is not None:
        # print information about the program
        print("\n")
        print("Name: " + name)
        print("Version: " + version)
        print("Description: " + description)
        print("Author: " + author_first_name + " " + author_last_name)
        print("\n")
        return True

    else:  # if don't have information
        print("Error: information")
        return False

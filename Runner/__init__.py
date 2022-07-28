from Runner.DevFileManager import *
from Runner.Execute import *
from Runner.Window import *


def start(run: str = "nothing", graphique: bool = False) -> Error:
    """
    start the program
    :param run: str, information or dump
    :param graphique: bool, if the program is run in graphique mode
    :return: Error, error if there is one
    """
    if graphique:
        try:
            Window(run=run)
        except Exception as e:
            print(e)
            return Error(success=False, message=str(e), code=5)
        else:
            return Error(success=True, message="Mode graphique was successfully run", code=200)
        # return fenetre(run=run)
    else:
        return Runner(run=run, graphique=graphique)

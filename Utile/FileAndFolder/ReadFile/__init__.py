import os
from Utile.FileAndFolder.ReadFile.File import *
from Utile.FileAndFolder.ReadFile.SqlFile import *
from Utile.FileAndFolder.ReadFile.DumpSqlFile import *
from Utile.FileAndFolder.ReadFile.TxtFile import *
from Utile.FileAndFolder.ReadFile.JsonFile import *


def existFile(path: str) -> bool:
    """
    check if file exist
    :param path: path to file
    :return: bool, True if exist, False if not
    """
    return os.path.isfile(path)

def generateFile(path: str, sp: str = None, debug: bool = False) -> None | file:
    """
    generate a read file
    :param path: path to file
    :param debug: debug mode
    :return:
    """
    if existFile(path):
        if path.split('.')[-1] == "sql":
            if sp == 'Dump':
                return dumpSqlFile(path=path)
            else:
                return SqlFile(path=path)
        elif path.split('.')[-1] == "txt":
            return TxtFile(path=path)
        elif path.split('.')[-1] == "json":
            return JsonFile(path=path)
        elif debug:
            print("file not found: " + path)
            return None
        else:
            print("File type not found")
            exit()
    else:
        print("File not found")
        print(path)
        print(sp)
        print(debug)
        exit()
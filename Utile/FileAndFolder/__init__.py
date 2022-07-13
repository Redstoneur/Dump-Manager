import shutil

from Utile.FileAndFolder.ReadFile import *
from Utile.FileAndFolder.ReadFoldersContained import *


# fonction pour déplacer un fichier dans un autre dossier
def moveFile(file: str, folder: str) -> None:
    """
    move a file in a folder
    :param file: str, file to move
    :param folder: str, folder to move the file
    :return: None
    """
    try:
        shutil.move(file, folder)
    except Exception as e:
        print(e)

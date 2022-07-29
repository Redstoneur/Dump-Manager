from Utilities import *
import os


def create(path: str) -> bool:
    if not existFolder(path):
        os.makedirs(path)
        return True
    else:
        return False


def Folder_Generator_Information_fr(path: str, nameFolder: str) -> None:
    if existFolder(path):
        print("Le dossier " + nameFolder + " existe déjà")
    else:
        print("Le dossier " + nameFolder + " n'existe pas")
        print("Le dossier " + nameFolder + " va être créé")
        if create(path):
            print("Le dossier " + nameFolder + " a été créé")
        else:
            print("Le dossier " + nameFolder + " n'a pas pu être créé")
            exit()


def Folder_Generator_Information_en(path: str, nameFolder: str) -> None:
    if existFolder(path):
        print("The folder " + nameFolder + " exists")
    else:
        print("The folder " + nameFolder + " does not exist")
        print("The folder " + nameFolder + " will be created")
        if create(path):
            print("The folder " + nameFolder + " has been created")
        else:
            print("The folder " + nameFolder + " could not be created")
            exit()

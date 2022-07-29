from Start.Variable import *
import Start.LibrairyUtilities as LibUtils
import Start.FolderGenerator as FolderGenerator
import Start.FileGenerator as FileGenerator
import time as t


def init(language: str = "fr", reboot: bool = False, s: int = 2) -> None:
    """
    Script to initialize the program
    :param language: str, language of the program
    :param reboot: bool, True if we want to reboot the program
    :param s: int, sleep time
    :return: None
    """
    if language == "fr":
        print("Initialisation of projet")
        print("-----------------------")
        print("")
        print("1. Vérifier la présence de la librairie propriétaire 'Utilities'")
        LibUtils.LibrairyUtilities_fr()
        from Utilities import existFile, CleanTerminal
        print("2. Création du Fichier README.md")
        FileGenerator.File_Generator_Information_fr(path=PathFileREADME, data=README)
        print("3. Génération du dossier Data")
        FolderGenerator.Folder_Generator_Information_fr(path=PathFolderData, nameFolder=NameFolderData)
        print("4. Génération du fichier package.json dans le dossier Data")
        FileGenerator.File_Generator_Information_fr(path=PathFilePackageJson, data=package)
        print("5. Génération du fichier Database-Information.json dans le dossier Data")
        if existFile(path=PathFileDatabaseInformation) and not reboot:
            print("Fichier déjà existant : " + PathFileDatabaseInformation)
        else:
            FileGenerator.File_Generator_Information_fr(path=PathFileDatabaseInformation, data=DatabaseInformation)
        print("6. Génération du dossier Dumps dans le dossier Data")
        FolderGenerator.Folder_Generator_Information_fr(path=PathFolderDumps, nameFolder=NameFolderDumps)
        print("6.1. Génération du fichier .Dumpps.md dans le dossier Dumps")
        FileGenerator.File_Generator_Information_fr(path=PathFileDumpsMd, data=Dumps)
        print("6.2. Génération du dossier lastDumpsFiles dans le dossier Dumps")
        FolderGenerator.Folder_Generator_Information_fr(path=PathFolderlastDumpsFiles,
                                                        nameFolder=NameFolderlastDumpsFiles)
        print("6.3. Génération du fichier lastDumpsFiles/.Information.md dans le dossier Dumps")
        FileGenerator.File_Generator_Information_fr(path=PathFileDumpsInformationMd, data=Information)
        print("")
        t.sleep(s)
        CleanTerminal()
    elif language == "en":
        print("Initialization of project")
        print("-----------------------")
        print("")
        print("1. Check the presence of the proprietary library 'Utilities'")
        LibUtils.LibrairyUtilities_en()
        from Utilities import existFile, CleanTerminal
        print("2. Creation of File README.md")
        FileGenerator.File_Generator_Information_en(path=PathFileREADME, data=README)
        print("3. Generation of folder Data")
        FolderGenerator.Folder_Generator_Information_en(path=PathFolderData, nameFolder=NameFolderData)
        print("4. Generation of file package.json in the folder Data")
        FileGenerator.File_Generator_Information_en(path=PathFilePackageJson, data=package)
        print("5. Generation of file Database-Information.json in the folder Data")
        if existFile(path=PathFileDatabaseInformation) and not reboot:
            print("File already exists : " + PathFileDatabaseInformation)
        else:
            FileGenerator.File_Generator_Information_en(path=PathFileDatabaseInformation, data=DatabaseInformation)
        print("6. Generation of folder Dumps in the folder Data")
        FolderGenerator.Folder_Generator_Information_en(path=PathFolderDumps, nameFolder=NameFolderDumps)
        print("6.1. Generation of file .Dumpps.md in the folder Dumps")
        FileGenerator.File_Generator_Information_en(path=PathFileDumpsMd, data=Dumps)
        print("6.2. Generation of folder lastDumpsFiles in the folder Dumps")
        FolderGenerator.Folder_Generator_Information_en(path=PathFolderlastDumpsFiles,
                                                        nameFolder=NameFolderlastDumpsFiles)
        print("6.3. Generation of file lastDumpsFiles/.Information.md in the folder Dumps")
        FileGenerator.File_Generator_Information_en(path=PathFileDumpsInformationMd, data=Information)
        print("")
        t.sleep(s)
        CleanTerminal()
    else:
        print("Language not supported")
        print("")
        print("Please use 'fr' or 'en'")
        print("")
        exit()


if __name__ == "__main__":
    init()

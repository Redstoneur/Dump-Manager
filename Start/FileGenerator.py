from Utilities import *


def initiationOfFile_fr(path: str):
    """
    generate a markdown file with information about the project
    :param data: str, data to write in file
    :return: None
    """
    if existFile(path):
        print("Fichier déjà existant : " + path)
    else:
        print("Fichier non existant : " + path)
        try:
            with open(path, 'w') as f:
                if path.split('.')[-1] == "json":
                    f.write("{}")
                else:
                    f.write("")
                f.close()
        except Exception as e:
            print(e)
            exit()
        print("Fichier initialisé avec succès : " + path)


def initiationOfFile_en(path: str):
    """
    generate a markdown file with information about the project
    :param data: str, data to write in file
    :return: None
    """
    if existFile(path):
        print("File already exists : " + path)
    else:
        print("File does not exist : " + path)
        try:
            with open(path, 'w') as f:
                if path.split('.')[-1] == "json":
                    f.write("{}")
                else:
                    f.write("")
                f.close()
        except Exception as e:
            print(e)
            exit()
        print("File initiated successfully : " + path)


def createFile(path: str, data: object) -> [bool, bool]:
    """
    create a markdown file
    :param path: str, path to file
    :param data: str, data to write in file
    :return: None
    """
    f = generateFile(path)
    if isinstance(f, MarkdownFile):
        f = MarkdownFile(path)
        if isinstance(data, str):
            f.write(data)
            return [True, True]
        else:
            return [True, False]
    elif isinstance(f, TxtFile):
        f = TxtFile(path)
        if isinstance(data, str):
            f.write(data)
            return [True, True]
        else:
            return [True, False]
    elif isinstance(f, JsonFile):
        f = JsonFile(path)
        if isinstance(data, dict):
            f.write(data)
            return [True, True]
        else:
            return [True, False]
    else:
        return [False, False]


def File_Generator_Information_fr(path: str, data: object) -> None:
    """
    generate a markdown file with information about the project
    :param data: str, data to write in file
    :return: None
    """
    initiationOfFile_fr(path)
    info: [bool, bool] = createFile(path, data)
    if info[0]:
        if info[1]:
            print("Fichier créé avec succès : " + path)
        else:
            print("Fichier créé avec succès " + \
                  "mais le contenu n'est pas dans le bon format donc il n'a pas ajouté : " + path)
    else:
        print("Fichier non créé : " + path)


def File_Generator_Information_en(path: str, data: object) -> None:
    """
    generate a markdown file with information about the project
    :param data: str, data to write in file
    :return: None
    """
    initiationOfFile_en(path)
    info: [bool, bool] = createFile(path, data)
    if info[0]:
        if info[1]:
            print("File created successfully : " + path)
        else:
            print("File created successfully " + \
                  "but the content is not in the right format so it did not add : " + path)
    else:
        print("File not created : " + path)

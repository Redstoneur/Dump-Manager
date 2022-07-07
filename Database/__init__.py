from Database.DatabaseExecutor import *
from Utile import *

DatabaseInfo: JsonFile = JsonFile("./Data/Database-Information.json")

# noinspection PyTypeChecker
DumpsPath: str = DatabaseInfo.get("path-dumps")
if DumpsPath is None or DumpsPath == "":
    DumpsPath = "./Data/Dumps"
FoldersContained: FoldersContained = FoldersContained(DumpsPath)


def mainVersionDB() -> Error:
    """
    dump all databases with a connection to the database
    :return: Error, True if the program worked, False if not
    """
    try:
        print('connecting to database')
        bd: databaseExecutor = databaseExecutor(user=DatabaseInfo.get("user"),
                                                password=DatabaseInfo.get("password"),
                                                host=DatabaseInfo.get("host"),
                                                port=DatabaseInfo.get("port"),
                                                name=DatabaseInfo.get("name"))
        print('connected to database')
        print('reading dumps')
        for folder in FoldersContained.folders:
            print('reading ' + folder.split('.')[0])
            sql: SqlFile = generateFile(path=DumpsPath + "/" + folder, debug=True)
            sql.read()
            bd.execute(sql.getData())
            print("Executed: " + sql.getPath())
            break
        print('dumps readed');

        print('closing connection')
        bd.close()
        print('connection closed')

        return Error(success=True, message="success", code=200)

    except Exception as e:
        return Error(success=False, message=str(e), code=500)

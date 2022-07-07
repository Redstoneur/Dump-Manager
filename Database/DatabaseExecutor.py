import mysql.connector as mysql


class databaseExecutor:
    name: str
    user: str
    password: str
    host: str
    port: int
    connection = None
    cursor = None

    def __init__(self, user: str, password: str, host: str, port: int, name: str = None):
        self.name: str = name
        self.user: str = user
        self.password: str = password
        self.host: str = host
        self.port: int = port
        self.connection = None
        self.cursor = None
        if self.name is not None:
            self.connectDB()
        else:
            self.connect()

    def connectDB(self):
        try:
            self.connection = mysql.connect(
                database=self.name,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(e)
            exit()

    def connect(self):
        try:
            self.connection = mysql.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(e)
            exit()

    def execute(self, query, values=None):
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
        except Exception as e:
            print(e)
            exit()

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()

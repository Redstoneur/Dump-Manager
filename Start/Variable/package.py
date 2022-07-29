package: dict = {
  "name": "Dump Manager",
  "version": "1.4.3",
  "date-created": "2022-07-06",
  "description-fr": "Dump Manager est un outil de gestion des dumps de bases de données. Il permet de gérer les dumps de bases de données et de les restaurer.",
  "description-en": "Dump Manager is a tool to manage database dumps. It allows you to manage database dumps and restore them.",
  "website": "",
  "license": "",
  "dependencies": {
    "python": ">=3.6",
    "pip": ">=7.0",
    "librairy": [
      {
        "name": "Database",
        "description-fr": "Librairie de gestion des bases de données",
        "description-en": "Database library",
        "use-fonction": [
          "mainVersionDB"
        ]
      },
      {
        "name": "abc",
        "description-fr": "Librairie pour la mise en place de classes abstraites",
        "description-en": "Library for abstract class implementation",
        "use-fonction": [
          "abstractmethod",
          "ABC"
        ]
      },
      {
        "name": "sys",
        "description-fr": "Librairie pour la gestion des variables système",
        "description-en": "Library for system variables management",
        "use-fonction": "*"
      }
    ]
  },
  "information_fr": "mettez votre dump dans le dossier './Dumps'",
  "information_en": "put your dump un the folder './Dumps'",
  "author": {
    "lastName": "SIMOES",
    "firstName": "Alipio",
    "birthDate": "2022-09-21",
    "email": "alipio.simoes01@gmail.com"
  }
}
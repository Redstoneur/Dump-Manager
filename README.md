# Application : Dump-Manager

## Sommaire

- [Dump-Manager](#dump-manager)
- [Dump-Manager-Installation](#dump-manager-installation)
- [Dump-Manager-Configuration](#dump-manager-configuration)
- [Dump-Manager-Usage](#dump-manager-usage)
- [Dump-Manager-Tests](#dump-manager-tests)
- [Dump-Manager-History](#dump-manager-history)

## Dump-Manager

Dump-Manager is a simple tool to manage dumps.
It simplifies to add a new dump in the database and to manage it.

## Dump-Manager-Installation

> not implemented

## Dump-Manager-Configuration

To configure Dump-Manager, you need to implement the JSON-file `./Data/Database-Information.json`

```json
{
  "host": "address of the database",
  "port": "port of the database",
  "user": "user of the database",
  "password": "password of the database",
  "name": "name of the database",
  // optional if you use a specific database and you use the DatabaseRunner
  "path-dumps": "path of the dumps",
  // optional if you use a specific folder for the dumps
  "script-dumps": "command to execute to create a dump"
  // optional if you use a specific command for the dumps and you use the ShellRunner
}
```

## Dump-Manager-Usage

To use Dump-Manager, you need to put dumps in the folder `./Data/Dumps`

## Dump-Manager-Tests

> not implemented

## Dump-Manager-History

1. when the project was created

    - the project was created in the year 2022 by Alipio SIMOES.

2. Why the project was created

    - the project was created to help me to add dumps to my database.
    - the project was created to help me to manage my database.

3. What is the current version of the project

    - the current version is 1.2.0


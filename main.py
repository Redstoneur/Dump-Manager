from Runner import *


def main(run: str, graphique: bool) -> Error:
    """
    main function of the program
    :param run: str, information or dump
    :param graphique: bool, True if we want to run the program in graphique mode
    :return: None
    """
    return Runner(run=run, graphique=graphique)


if __name__ == '__main__':
    # recuperation of the arguments
    if len(sys.argv) > 1:
        run = sys.argv[1]
    else:
        run = "shell"

    # run the program
    result: Error = main(run=run, graphique=True)

    # if in debug mode, wait for the user to press a key
    if not result.success and result.code != 200:
        print("\n" + result.__str__() + "\n")
        input("Press Enter to continue...")
        sys.exit(result.code)
    else:
        sys.exit(result.code)

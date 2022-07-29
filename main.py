from Runner import *
from Start import *


def main(run: str, graphique: bool = True) -> Error:
    """
    main function of the program
    :param run: str, information or dump
    :param graphique: bool, True if we want to run the program in graphique mode
    :return: Error, error if there is one
    """
    return start(run=run, graphique=graphique)


if __name__ == '__main__':
    language: str = 'fr'
    reboot: bool = False
    run: str = "shell"
    graphique: bool = True

    # recuperation of the arguments
    if len(sys.argv) > 1:
        language = sys.argv[1]
    if len(sys.argv) > 2:
        reboot = sys.argv[2] == "True"
    if len(sys.argv) > 3:
        run = sys.argv[3]
    if len(sys.argv) > 4:
        graphique = sys.argv[4] == "True"

    try:
        import reboot as r
    except ImportError:
        try:
            with open("./reboot.py", 'w') as f:
                f.write("reboot=True")
                f.close()
            reboot = True
        except Exception as e:
            print(e)
            exit()
        else:
            import reboot as r

    if r.reboot != reboot:
        r.reboot = reboot
    init(language=language, reboot=r.reboot)


    # run the program
    result: Error = main(run=run, graphique=graphique)

    # if in debug mode, wait for the user to press a key
    if not result.success and result.code != 200:
        print("\n" + result.__str__() + "\n")
        input("Press Enter to continue...")
        sys.exit(result.code)
    else:
        sys.exit(result.code)

#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print("{} argument" .format((len(argv) - 1)), end="")
    if len(argv) == 2:
        print(":\n{}: {}" .format(1, argv[1]))
    elif len(argv) > 2:
        print("s:")
        for i in range(1, len(argv)):
            print("{}: {}" .format(i, argv[i]))
    else:
        print("s.")

#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for name in dir(hidden_4):
        if not name.startwith("__"):
            print("{}" .format(name))

#!/usr/bin/python3
if __name__ == ("__main__"):
    from calculator_1 import add, sub, div, mul
    from sys import argv
    operators = ["+", "-", "*", "/"]
    if not len(argv) == 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if not argv[2] in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        elif argv[2] = "+":
            print("{} + {} = {}" .format(int(argv[1]), int(argv[3]), add(argv[1], argv[3])))
        elif argv[2] = "-":
            print("{} - {} = {}" .format(int(argv[1]), int(argv[3]), sub(argv[1], argv[3])))
        elif argv[2] = "*":
            print("{} * {} = {}" .format(int(argv[1]), int(argv[3]), mul(argv[1], argv[3])))
        else:
            print("{} / {} = {}" .format(int(argv[1]), int(argv[3]), div(argv[1], argv[3])))
        exit(0)

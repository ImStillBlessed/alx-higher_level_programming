#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    from sys import argv

    operators = ["+", "-", "*", "/"]

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a, operator, b = argv[1], argv[2], argv[3]

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a, b = int(a), int(b)

    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = sub(a, b)
    elif operator == "*":
        result = mul(a, b)
    elif operator == "/":
        result = div(a, b)

    print("{} {} {} = {}".format(a, operator, b, result))


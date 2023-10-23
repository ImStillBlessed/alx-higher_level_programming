#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        value = None
        value = a / b
    except Exception:
        pass
    finally:
        print("Inside result: {}".format(value))
        return value

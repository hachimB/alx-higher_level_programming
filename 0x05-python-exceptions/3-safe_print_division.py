#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        if (b != 0):
            div = a / b
        else:
            div = None
        return (div)
    except Exception:
        print("not possible")
    finally:
        print("Inside result: {}".format(div))

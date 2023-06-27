#!/usr/bin/python3


def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except Exception as excep:
        sys.stderr.write("Exception: " + str(excep) + "\n")
        return False

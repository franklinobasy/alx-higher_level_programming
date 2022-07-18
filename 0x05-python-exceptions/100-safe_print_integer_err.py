import sys

def safe_print_integer_err(value):
    try:
        r = value / 1
        print("{:d}".format(value))
        return True
    except TypeError as e:
        sys.stderr.write("Exception: " + e.args[0])
        return False

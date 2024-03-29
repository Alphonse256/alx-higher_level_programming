#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    argc = len(sys.argv) - 1
    operator = {"+": add, "-": sub, "*": mul, "/": div}

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        if sys.argv[2] not in list(operator.keys()):
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            result = operator[sys.argv[2]](a, b)
            print("{} {} {} = {}".format(a, sys.argv[2], b, result))

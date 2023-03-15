#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    output = 0
    for index in range(1, argc):
        output += int(sys.argv[index])
    print("{}".format(output))

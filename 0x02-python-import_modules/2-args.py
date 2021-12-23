#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    lon = len(argv)
    if lon == 1:
        print("{} {:s}.".format(lon - 1, "arguments"))
    elif lon == 2:
        print("{} {:s}:".format(lon - 1, "argument"))
    elif lon >= 2:
        print("{} {:s}:".format(lon - 1, "arguments"))
    for index in range(1, lon):
        print("{}: {:s}".format(index, argv[index]))

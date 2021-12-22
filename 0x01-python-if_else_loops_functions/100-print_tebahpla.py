#!/usr/bin/python3
for x in range(122, 96, -1):
    print("{:c}".format(x if x % 2 == 0 else x - 32), end="")

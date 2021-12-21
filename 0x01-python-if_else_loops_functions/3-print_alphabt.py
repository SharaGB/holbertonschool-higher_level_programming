#!/usr/bin/python3
for i in range((97), (122) + 1):
    if chr(i) != (101) and chr(i) != (113):
        print("{:c}".format(i), end='')

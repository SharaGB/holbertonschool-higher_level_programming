#!/usr/bin/python3
for i in range((97), (122) + 1):
    if chr(i) != 'e' and chr(i) != 'q':
        print("{:c}".format(i), end='')

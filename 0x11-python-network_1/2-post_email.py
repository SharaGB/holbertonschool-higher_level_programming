#!/usr/bin/python3
""" Sends a POST request to the passed URL with the email as a parameter,
        and displays the body of the response """
import urllib.parse
import urllib.request
from sys import argv

if __name__ == '__main__':
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values).encode('utf-8')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))

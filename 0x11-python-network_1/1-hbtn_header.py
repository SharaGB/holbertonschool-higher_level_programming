#!/usr/bin/python3
""" Sends a request to the URL and displays the value of the X-Request-Id
        variable found in the header of the response. """
import urllib.request
from sys import argv

if __name__ == '__main__':
    URL = urllib.request.Request(argv[1])
    with urllib.request.urlopen(URL) as request:
        print(request.headers['X-Request-Id'])

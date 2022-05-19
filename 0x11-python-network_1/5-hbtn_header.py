#!/usr/bin/python3
""" Sends a request to the URL and displays the value of the
    variable X-Request-Id in the response header. """
from requests import get
from sys import argv

if __name__ == '__main__':
    request = get(argv[1])
    print(request.headers.get('X-Request-Id'))

#!/usr/bin/python3
""" Sends a request to the URL and displays the body of the response """
from requests import get
from sys import argv

if __name__ == '__main__':
    URL = get(argv[1])
    if URL.status_code >= 400:
        print('Error code: {}'.format(URL.status_code))
    else:
        print(URL.text)

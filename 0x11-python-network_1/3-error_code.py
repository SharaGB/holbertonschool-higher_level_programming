#!/usr/bin/python3
""" Sends a request to the URL and displays the body of the response """
import urllib.error
import urllib.request
from sys import argv

if __name__ == '__main__':
    URL = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(URL) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(str(e)))

#!/usr/bin/python3
""" Sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8) """
import urllib.parse
import urllib.request
from sys import argv

if __name__ == '__main__':
    URL = urllib.request.Request(argv[1])
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    req = urllib.request.Request(URL, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))

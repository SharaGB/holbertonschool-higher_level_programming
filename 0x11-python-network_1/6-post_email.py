#!/usr/bin/python3
""" Sends a POST request to the passed URL with the email as a parameter,
        and finally displays the body of the response. """
from requests import post
from sys import argv

if __name__ == '__main__':
    response = post(argv[1], {'email': argv[2]})
    print(response.text)

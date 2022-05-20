#!/usr/bin/python3
""" Takes your GitHub credentials (username and password) and
        uses the GitHub API to display your id """
from requests import get
from sys import argv

if __name__ == '__main__':
    USER = argv[1]
    PASSWORD = argv[2]
    response = get('https://api.github.com/user', auth=(USER, PASSWORD))
    print(response.json().get('id'))

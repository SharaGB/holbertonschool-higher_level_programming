#!/usr/bin/python3
""" Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter. """
from requests import post, get
from sys import argv

if __name__ == '__main__':
    URL = 'http://0.0.0.0:5000/search_user'
    if len(argv) <= 1:
        q = ""
    else:
        q = argv[1]
    try:
        request = post(URL, data={'q': q})
        json = request.json()
        ID = json.get('id')
        NAME = json.get('name')
        if len(json) != 0:
            print('[{}] {}'.format(ID, NAME))
        else:
            print('No result')
    except Exception as e:
        print('Not a valid JSON')

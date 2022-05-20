#!/usr/bin/python3
""" List 10 commits (from the most recent to oldest)
        of the repository “rails” """
from requests import get
from sys import argv

if __name__ == '__main__':
    request = get('https://api.github.com/repos/{}/{}/commits'
                  .format(argv[2], argv[1]))
    commits = request.json()
    for repo in commits[:10]:
        print("{}: {}".format(repo.get('sha'),
                              repo.get('commit').get('author').get('name')))

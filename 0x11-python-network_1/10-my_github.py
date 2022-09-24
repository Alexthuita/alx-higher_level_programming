#!/usr/bin/python3

"""Uses the GitHub API to display a GitHub ID based on given credentials."""

if __name__ == "__main__":
    import sys
    import requests
    r = requests.get('https://api.github.com/user',
                     auth=(sys.argv[1], sys.argv[2]))
    print(r.json().get('id'))

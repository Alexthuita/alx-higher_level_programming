#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email."""

if __name__ == "__main__":
    import sys
    import urllib.parse
    import urllib.request
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    request = urllib.request.Request(sys.argv[1], data=data)
    with urllib.request.urlopen(request) as response:
        the_page = response.read().decode('utf-8')
        print(the_page)

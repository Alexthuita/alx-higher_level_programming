#!/usr/bin/python3

"""fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests
    req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("	- type:", type(req.text))
    print("	- content:", req.text)


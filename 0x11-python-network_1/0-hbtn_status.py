#!/usr/bin/python3
# fetches https://alx-intranet.hbtn.io/status


import urllib
if (__name__ == "__main__"):
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print(f"- type: {type(body)}")
        print(f"- content: {body}")
        print(f"- utf8 content: {body.decode()}")

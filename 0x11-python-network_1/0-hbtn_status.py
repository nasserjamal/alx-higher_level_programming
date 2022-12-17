#!/usr/bin/python3
# fetches https://alx-intranet.hbtn.io/status

import urllib.request
if(__name__ == "__main__"):
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        body = response.read()
        print(f"- type: {type(body)}")
        print(f"- content: {body}")
        print(f"- utf8 content: {body.decode()}")

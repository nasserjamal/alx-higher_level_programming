#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status """


if (__name__ == "__main__"):
    import requests
    url = "https://alx-intranet.hbtn.io/status"
    resp = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type(resp.text)}")
    print(f"\t- content: {resp.text}")

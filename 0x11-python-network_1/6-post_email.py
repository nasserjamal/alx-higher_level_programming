#!/usr/bin/python3
"""
Sends a post request to a server
"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    response = requests.post(url, data=data)
    print(response.text)

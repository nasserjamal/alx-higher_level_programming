#!/usr/bin/python3
"""
takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the
letter as a parameter.
"""

if __name__ == "__main__":
    import sys
    import requests
    msg = ""
    if len(sys.argv) > 1:
        msg = sys.argv[1] 
    response = requests.post("http://0.0.0.0:5000/search_user",params={'q': msg})
    try:
        jsonData = response.json()
        if len(jsonData) > 0:
            print("No result")
        else:
            print(f"[{jsonData.get('id')}] {jsonData.get('name')}")
    except requests.exceptions.JSONDecodeError as e:
        print("Not a valid JSON")


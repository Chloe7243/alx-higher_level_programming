#!/usr/bin/python3
"""
A Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import requests
from sys import argv


if __name__ == "__main__":
    param = {'q': '' if len(argv) < 2 else argv[1]}
    res = requests.post('http://0.0.0.0:5000/search_user', data=param)
    try:
        data = res.json()
        if (len(data) == 0):
            print("No result")
        else:
            print(f"{[data.get('id')]} {data.get('name')}")
    except ValueError as e:
        print("Not a valid JSON")

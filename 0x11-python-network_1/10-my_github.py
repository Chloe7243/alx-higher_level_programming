#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
from sys import argv


if __name__ == "__main__":
    try:
        auth = (argv[1], argv[2])
        res = requests.get(f"https://api.github.com/user", auth=auth)
        print(res.json().get('id'))
    except ValueError as e:
        print(None)

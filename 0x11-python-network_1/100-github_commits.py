#!/usr/bin/python3
"""
A Python script that list 10 commits (from the most recent to oldest)
"""
import requests
from sys import argv


if __name__ == "__main__":
    try:
        url = f"https://api.github.com/repos/{argv[1]}/{argv[2]}/commits"
        res = requests.get(url)
        data = res.json()
        for i in range(10):
            res = f"{data[i]['sha']}: {data[i]['commit']['author']['name']}"
            print(res)
    except ValueError as e:
        print(None)

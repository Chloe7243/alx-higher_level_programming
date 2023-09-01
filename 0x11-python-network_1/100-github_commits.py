#!/usr/bin/python3
""" A Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id """
import requests
from sys import argv


if __name__ == "__main__":
    try:
        res = requests.get(f"https://api.github.com/repos/{argv[1]}/{argv[2]}/commits")
        data = res.json()
        for i in range(10):
            print(f"{data[i]['sha']}: {data[i]['commit']['author']['name']}")
    except ValueError as e:
        print(None)

#!/usr/bin/python3
"""  a Python script that fetches https://alx-intranet.hbtn.io/status """
import requests
from sys import argv


if __name__ == "__main__":
    try:
        res = requests.get(argv[1])
        status = res.raise_for_status()
        if (status is None):
            print(res.text)
    except requests.exceptions.HTTPError as e:
        print(f"Error code: {str(e)[:3]}")

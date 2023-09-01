#!/usr/bin/python3
"""  a Python script that fetches https://alx-intranet.hbtn.io/status """
from urllib import request
from sys import argv

if __name__ == "__main__":
    with request.urlopen(argv[1]) as res:
        print(res.headers.get("X-Request-Id"))

#!/usr/bin/python3
"""
Takes in URL and an email and sends POST request to passed URL
"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    values = dict(email=argv[2])
    url = argv[1]
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        html_page = response.read().decode("utf-8")
        print(html_page)

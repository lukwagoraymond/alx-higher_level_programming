#!/usr/bin/python3
"""
Displays response body with email passed to URL using POST request
"""
import requests
from sys import argv

if __name__ == "__main__":
    data = {'email': argv[2]}
    url = argv[1]
    r = requests.post(url, data=data)
    print(r.text)

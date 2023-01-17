#!/usr/bin/python3
"""
Takes GitHub credentials and uses the Github API to display your id
"""
from sys import argv
import requests

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    r = requests.get('https://api.github.com/user', auth=(username, password))
    print(r.json().get('id'))

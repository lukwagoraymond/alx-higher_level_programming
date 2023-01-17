#!/usr/bin/python3
"""
Takes a letter as parameter and sends a POST request to url
"""
from sys import argv
import requests


if __name__ == "__main__":
    letter = "" if len(argv) == 1 else argv[1]
    payload = {"q": letter}
    url = "http://0.0.0.0:5000/search_user"

    r = requests.post(url, data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")

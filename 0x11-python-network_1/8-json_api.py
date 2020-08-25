#!/usr/bin/python3
""" send POST request """
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sr = {"q": ""}
    else:
        sr = {"q": sys.argv[1]}
    response = requests.post("http://0.0.0.0:5000/search_user", data=sr)
    try:
        result = response.json()
        print(result)
    except ValueError:
        print("Not a valid JSON")

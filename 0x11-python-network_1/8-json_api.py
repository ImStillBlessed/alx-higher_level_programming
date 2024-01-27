#!/usr/bin/python3
"""
 script that takes in a letter and sends a POST request
 to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    q = ""
    if sys.argv[1]:
        q = sys.argv[2]
    try:
        response = requests.post(url, data={'q': q})
        json_data = response.json()
        if json_data:
            print(f"[{json_data.get('id')}] {json_data.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

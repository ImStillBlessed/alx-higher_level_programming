#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    page = requests.get(url)
    print(f"""Body response:
- type: {type(page.text)}
- content: {page.content.decode('utf-8')}""" )

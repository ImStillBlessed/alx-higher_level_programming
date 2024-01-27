#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


url = 'https://alx-intranet.hbtn.io/status'
if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print(f"Body response:")
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")
        print(f"\t- utf8 content: {html.decode('utf8')}")

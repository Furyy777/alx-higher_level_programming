#!/usr/bin/python3
"""
Python script that fetches an URL with requests package
"""
import requests


if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    t = r.text
    print('Body response:')
    print('\t- type: {}'.format(type(t)))
    print('\t- content: {}'.format(t))

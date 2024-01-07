#!/usr/bin/python3
"""Module documentation"""
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status")\
            as response:
        content = response.read()
        utf8_content = content.decode("utf-8")
    print("Body response:")
    print("    - type:", type(content))
    print("    - content:", content)
    print("    - utf8 content:", utf8_content)

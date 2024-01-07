#!/usr/bin/python3
"""Module documentation"""
import urllib.request


if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')
    display = """Body response:
        - type: {}
        - content: {}
        - utf8 content: {}""".format(type(content), content, utf8_content)

    print(display)

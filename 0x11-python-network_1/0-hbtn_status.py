#!/usr/bin/python3
"""Module documentation"""
import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.read()
    utf8_content = content.decode('utf-8')

display = """Body response:
    - type: {}
    - content: {}
    - utf8 content: {}""".format(type(content), content, utf8_content)

print(display)

#!/usr/bin/python3
"""That's the module documentaion"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    m_list = load_from_json_file("add_item.json")
except Exception:
    m_list = []

for i in sys.argv:
    if not (i == sys.argv[0]):
        m_list.append(i)
save_to_json_file(m_list, "add_item.json")

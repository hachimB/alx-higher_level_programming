#!/usr/bin/python3
"""Module documentation"""
import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)
    connection = MySQLdb.connect(host='localhost',
                                 port=3306,
                                 user=sys.argv[1],
                                 passwd=sys.argv[2],
                                 db=sys.argv[3])
    cur = connection.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id".
        format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    connection.close()

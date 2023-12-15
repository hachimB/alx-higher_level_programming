#!/usr/bin/python3
"""module documentation"""
import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    connection = MySQLdb.connect(host='localhost',
                                 port=3306,
                                 user='root',
                                 passwd='',
                                 db='hbtn_0e_0_usa')
    cur = connection.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    connection.close()

#!/usr/bin/python3
"""Module documentation"""
import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)
    user_input = sys.argv[4]
    connection = MySQLdb.connect(host='localhost',
                                 port=3306,
                                 user='root',
                                 passwd='',
                                 db='hbtn_0e_0_usa')
    cur = connection.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cur.execute(query, (user_input,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    connection.close()

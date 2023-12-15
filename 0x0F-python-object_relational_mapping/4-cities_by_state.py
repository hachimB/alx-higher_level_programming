#!/usr/bin/python3
"""Module documentation"""
import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    connection = MySQLdb.connect(host='localhost',
                                 port=3306,
                                 user='root',
                                 passwd='',
                                 db='hbtn_0e_4_usa')
    cur = connection.cursor()
    query = "SELECT cities.id, cities.name, states.name\
 FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    connection.close()

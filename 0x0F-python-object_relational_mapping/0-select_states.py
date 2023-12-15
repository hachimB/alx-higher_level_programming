#!/usr/bin/python3
"""Module documentation"""
import MySQLdb


if __name__ == "__main__":
    con = MySQLdb.connect(host='localhost',
                          port=3306,
                          user='root',
                          passwd='',
                          db='hbtn_0e_0_usa')
    cur = con.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    con.close()

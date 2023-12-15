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
                                 user=sys.argv[1],
                                 passwd=sys.argv[2],
                                 db=sys.argv[3])
    cur = connection.cursor()
    query = "SELECT cities.name FROM cities INNER JOIN states\
 ON cities.state_id = states.id WHERE states.name LIKE BINARY %s"
    cur.execute(query, (user_input,))
    rows = cur.fetchall()
    city = []
    for row in rows:
        city.append(row[0])
    r = ', '.join(city)
    print(r)
    cur.close()
    connection.close()

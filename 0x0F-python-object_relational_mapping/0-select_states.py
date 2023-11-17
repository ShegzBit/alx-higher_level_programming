#!/usr/bin/python3
"""
A module to select all states in states table
ordered by id in asc
Using MySQL
"""

import MySQLdb
import sys


if __name__ == "__main__":
    args = sys.argv[1:]

    usr, passwd, dtb = args
    db = MySQLdb.connect(host="localhost", user=usr, passwd=passwd,
                         port=3306, db=dtb, charset="utf8")
    cursor = db.cursor()

    command = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(command)
    table = cursor.fetchall()
    for row in table:
        print(row)
    cursor.close()
    db.close()

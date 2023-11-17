#!/usr/bin/python3
"""
A module that prints all state in states
starting with N ordered in asc by id
"""

import MySQLdb
import sys


if __name__ == "__main__":
    _, user, passwd, db = sys.argv

    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=passwd, db=db, charset="utf8")
    cursor = db.cursor()

    command = "SELECT * FROM states WHERE BINARY name\
 LIKE 'N%' ORDER BY id ASC"

    cursor.execute(command)
    table = cursor.fetchall()
    for row in table:
        print(row)
    cursor.close()
    db.close()

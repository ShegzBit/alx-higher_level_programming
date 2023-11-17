#!/usr/bin/python3
"""
a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    _, user, passwd, db, name = sys.argv

    db = MySQLdb.connect('localhost', user=user, passwd=passwd,
                         db=db, port=3306, charset="utf8")
    cur = db.cursor()

    command = ("SELECT * FROM states WHERE BINARY name LIKE '{}' ORDER BY id\
 ASC".format(name))

    cur.execute(command)
    table = cur.fetchall()
    for row in table:
        print(row)
    cur.close()
    db.close()

#!/usr/bin/python3
"""
a script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. But this time,
write one that is safe from MySQL injections!
"""

import MySQLdb
import sys

if __name__ == "__main__":
    _, user, passwd, db, name = sys.argv
    db = MySQLdb.connect('localhost', user=user, passwd=passwd, db=db)
    cur = db.cursor()

    command = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(command, (name,))
    table = cur.fetchall()
    for row in table:
        print(row)
    cur.close()
    db.close()

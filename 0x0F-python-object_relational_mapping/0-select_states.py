#!/usr/bin/python3
"""
A module to select all states in states table
ordered by id in asc
Using MySQL
"""

import MySQLdb
import sys


args = sys.argv[1:]

db = MySQLdb.connect(host="localhost", user=args[0],
                     passwd=args[1], db=args[2])
cursor = db.cursor()

command = "SELECT * FROM states ORDER BY id ASC"
cursor.execute(command)
table = cursor.fetchall()
for row in table:
    print(row)

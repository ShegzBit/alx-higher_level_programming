#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    _, user, passwd, db = sys.argv
    db = MySQLdb.connect('localhost', user=user, passwd=passwd,
                         db=db)
    cs = db.cursor()

    command = "SELECT cities.id, cities.name, states.name\
 FROM cities JOIN states ON states.id = cities.state_id\
 ORDER BY states.id ASC"
    cs.execute(command)
    table = cs.fetchall()
    for row in table:
        print(row)
    cs.close()
    db.close()

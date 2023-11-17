#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    _, usr, pswd, dtb, state = sys.argv
    db = MySQLdb.connect('localhost', user=usr, passwd=pswd, db=dtb)
    cs = db.cursor()

    command = """
    SELECT cities.name FROM cities\
    JOIN states ON cities.state_id = states.id\
    WHERE states.id = \
    (SELECT id FROM states\
    WHERE states.name = %s)\
    ORDER BY cities.id ASC;\
    """
    cs.execute(command, (state,))
    table = cs.fetchall()
    cities = []
    for row in table:
        cities.extend(row)
    print(', '.join(cities))
    cs.close()
    db.close()

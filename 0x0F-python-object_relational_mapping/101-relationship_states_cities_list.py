#!/usr/bin/python3
"""
a script that lists all State objects, and corresponding City
objects, contained in the database hbtn_0e_101_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from relationship_city import Base, State, City


if __name__ == "__main__":
    _, user, passwd, dbname = sys.argv
    host = f"mysql://{user}:{passwd}@localhost:3306/{dbname}"
    engine = create_engine(host)
    Session = sessionmaker(engine)

    session = Session()

    rows = (session.query(City.id, City.state_id, City.name, State.name).
            join(State, State.id == City.state_id).
            order_by(State.id, City.id))
    states = []

    for c_id, s_id, cn, sn in rows:
        if sn in states:
            print(f"\t{c_id}: {cn}")
        else:
            print(f"{s_id}: {sn}")
            states.append(sn)

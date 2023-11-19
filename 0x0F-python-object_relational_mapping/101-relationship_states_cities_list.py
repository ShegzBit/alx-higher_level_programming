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

    check = session.query

    states = check(State.id, State.name).order_by(State.id)
    for state in states.all():
        cities = (check(City.id, City.name).
                  filter_by(state_id=state.id).order_by(City.id))
        print(f"{state[0]}: {state[1]}")
        for city in cities.all():
            print(f"\t{city[0]}: {city[1]}")
    session.close()

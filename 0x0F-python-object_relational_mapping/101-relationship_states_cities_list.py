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

    states = session.query(State).order_by(State.id)

    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

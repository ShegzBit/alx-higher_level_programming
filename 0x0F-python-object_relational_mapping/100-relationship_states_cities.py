#!/usr/bin/python3
"""
a script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa: (100-relationship_states_cities.py)
"""

from sqlalchemy import (create_engine, Table, Column,
                        Integer, String, ForeignKey)
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, State, City
import sys


if __name__ == "__main__":
    _, user, passwd, dbname = sys.argv
    host = f"mysql://{user}:{passwd}@localhost:3306/{dbname}"
    engine = create_engine(host)
    Session = sessionmaker(engine)

    Base.metadata.create_all(engine)
    session = Session()

    cali = State(name="California", cities=[City(name="San Francisco")])
    session.add(cali)
    session.commit()

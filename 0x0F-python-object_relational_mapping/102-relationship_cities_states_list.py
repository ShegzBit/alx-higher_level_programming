#!/usr/bin/python3
"""
a script that lists all City objects from the database hbtn_0e_101_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, State, City
import sys

if __name__ == "__main__":
    _, user, passwd, dbname = sys.argv
    host = f"mysql://{user}:{passwd}@localhost:3306/{dbname}"
    engine = create_engine(host)
    Session = sessionmaker(engine)

    session = Session()

    cities = session.query(City).order_by(City.id)

    for city in cities.all():
        print(f"{city.id}: {city.name} -> {city.state.name}")

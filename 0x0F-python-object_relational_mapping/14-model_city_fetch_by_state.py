#!/usr/bin/python3
"""
a script 14-model_city_fetch_by_state.py that prints all City
objects from the database hbtn_0e_14_usa
"""

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
import sys


if __name__ == "__main__":
    _, user, passwd, dbname = sys.argv
    host = f"mysql://{user}:{passwd}@localhost:3306/{dbname}"
    engine = create_engine(host)
    Session = sessionmaker(bind=engine)

    session = Session()

    cities = (session.query(City, State).filter
              (City.state_id == State.id).order_by(City.id).all())
    for city in cities:
        print(f"{city[-1].name}: ({city[0].id}) {city[0].name}")

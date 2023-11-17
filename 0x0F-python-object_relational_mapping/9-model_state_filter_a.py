#!/usr/bin/python3
"""
a script that lists all State objects that contain the
letter a from the database hbtn_0e_6_usa
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    _, user, passwd, dbname = sys.argv
    host = f"mysql://{user}:{passwd}@localhost:3306/{dbname}"
    engine = create_engine(host)
    Session = sessionmaker(engine)
    session = Session()

    states = (session.query(State).filter
                           (State.name.contains("a")).order_by(State.id).all())

    for count, state in enumerate(states):
        print(f"{count + 1}: {state.name}")

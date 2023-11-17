#!/usr/bin/python3
"""
a script that lists all State objects from the
database hbtn_0e_6_usa
"""

from sqlalchemy.orm import declarative_base as base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State


if __name__ == "__main__":
    _, user, passwd, dbname = sys.argv
    host = f"mysql://{user}:{passwd}@localhost:3306/{dbname}"
    engine = create_engine(host)
    Session = sessionmaker(engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for count, state in enumerate(states):
        print(f"{count + 1}: {state.name}")

#!/usr/bin/python3
"""
a script that prints the first State object from
the database hbtn_0e_6_usa
"""

from sqlalchemy.orm import declarative_base as base
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

    first = session.query(State).order_by(State.id).first()
    print("Nothing") if first is None else print(f"{1}: {first.name}")

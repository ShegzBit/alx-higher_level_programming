#!/usr/bin/python3
"""
a script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys


if __name__ == "__main__":
    _, user, passwd, dbname = sys.argv
    host = f"mysql://{user}:{passwd}@localhost:3306/{dbname}"
    engine = create_engine(host)
    Session = sessionmaker(engine)

    session = Session()

    session.query(State).filter(State.name.contains("a")).delete()
    session.commit()

    session.close()

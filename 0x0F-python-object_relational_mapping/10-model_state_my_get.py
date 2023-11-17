#!/usr/bin/python3
"""
a script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys
from model_state import Base, State


if __name__ == "__main__":
    _, user, passwd, dbname, name = sys.argv
    host = f"mysql://{user}:{passwd}@localhost:3306/{dbname}"
    engine = create_engine(host)
    Session = sessionmaker(engine)
    session = Session()

    state = session.query(State).filter(State.name == name).first()
    print("Not found") if state is None else print(state.id)

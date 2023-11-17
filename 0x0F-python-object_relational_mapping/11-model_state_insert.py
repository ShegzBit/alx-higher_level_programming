#!/usr/bin/python3
"""
a script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    _, user, passwd, dbname = sys.argv

    host = f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{dbname}"
    engine = create_engine(host)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="Louisiana")
    session.add(state)
    session.commit()
    print(state.id)
    session.close()

#!/usr/bin/python3
"""
a script that changes the name of a State object
from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    _, user, passwd, dbname = sys.argv
    host = f"mysql://{user}:{passwd}@localhost:3306/{dbname}"
    engine = create_engine(host)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()
    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()
    session.close()

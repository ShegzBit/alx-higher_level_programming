#!/usr/bin/python3
"""
a Python file similar to model_state.py named model_city.py
that contains the class definition of a City
"""

from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, Integer, ForeignKey
from relationship_state import Base, State


class City(Base):
    """
    City class for cities of a state
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id))

#!/usr/bin/python3
"""
a python file that contains the class definition of a State
and an instance Base = declarative_base()
"""

from sqlalchemy.orm import declarative_base as base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import String, Table, Column, Integer, ForeignKey
import sys


Base = base()


class State(Base):
    """
    the class definition of a State
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

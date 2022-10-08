#!/usr/bin/python3
'''
A python file that contains the class definition of a State
and an instance Base = declarative_base()
'''

from importlib_metadata import metadata
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class State(Base):
    '''
    Class with id and name attributes of each state
    '''

    __tablename__ = "state"
    id = Column(Integer, nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)

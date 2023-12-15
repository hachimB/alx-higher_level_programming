#!/usr/bin/python3
"""Module documentation"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """State class"""
    __tablename__ = 'states'
    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, unique=True,
                primary_key=True, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)

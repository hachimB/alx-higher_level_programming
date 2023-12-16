#!/usr/bin/python3
"""Module documetation"""
from sqlalchemy import Integer, String, create_engine, ForeignKey, Column
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """City class"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True, primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

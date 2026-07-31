#!/usr/bin/python3
"""Defines the State class and declarative Base for SQLAlchemy."""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """Represents a state, mapped to the MySQL table `states`."""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)

#!/usr/bin/python3
"""
This module defines the City class that links to the 'cities' table.
"""

from model_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class City(Base):
    """
    City class that inherits from Base.
    Links to the 'cities' MySQL table.
    """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

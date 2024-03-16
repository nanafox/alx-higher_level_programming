#!/usr/bin/python3

"""This module defines the City object class."""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from model_state import Base


class City(Base):
    """Defines the City object."""

    __tablename__ = "cities"
    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True,
        unique=True,
    )

    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    city = relationship("State", backref=backref("cities", order_by=id))

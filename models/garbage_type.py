#!/usr/bin/python
""" holds class Garbage_type"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Garbage_type(BaseModel, Base):
    """Representation of Garbage_type """
    if models.storage_t == 'db':
        __tablename__ = 'garbage_types'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Garbage_type"""
        super().__init__(*args, **kwargs)

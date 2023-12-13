#!/usr/bin/python3
""" holds class Garbage_collection_company"""
import models
from models.base_model import BaseModel, Base
from models.garbage_type import Garbage_type
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Garbage_collection_company(BaseModel, Base):
    """Representation of garbage_collection_company"""
    if models.storage_t == "db":
        __tablename__ = 'garbage_collection_companies'
        name = Column(String(128), nullable=False)
        garbage_types = relationship("Garbage_type", backref="garbage_collection_company")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes garbage_collection_company"""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def garbage_types(self):
            """getter for list of garbage_type instances related to the garbage_collection_company"""
            garbage_type_list = []
            all_garbage_types = models.storage.all(Garbage_type)
            for garbage_type in all_garbage_types.values():
                if garbage_type.garbage_collection_company_id == self.id:
                    garbage_type_list.append(garbage_type)
            return garbage_type_list

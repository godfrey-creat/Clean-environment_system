#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.garbage_collection_company import Garbage_collection_company
from models.base_model import BaseModel, Base
from models.user import Clients
from models.garbage_type import Garbage_type
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Client": Client, "Garbage_type": Garbage_type,
           "Garbage_collection_company": Garbage_collection_company}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        MAZINGIRABORA_MYSQL_CLIENT = getenv('MAZINGIRABORA_MYSQL_CLIENT')
        MAZINGIRABORA_MYSQL_PWD = getenv('MAZINGIRABORA_MYSQL_PWD')
        MAZINGIRABORA_MYSQL_HOST = getenv('MAZINGIRABORA_MYSQL_HOST')
        MAZINGIRABORA_MYSQL_DB = getenv('MAZINGIRABORA_MYSQL_DB')
        MAZINGIRABORA_ENV = getenv('MAZINGIRABORA_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(MAZINGIRABORA_MYSQL_CLIENT,
                                             MAZINGIRABORA_MYSQL_PWD,
                                             MAZINGIRABORA_MYSQL_HOST,
                                             MAZINGIRABORA_MYSQL_DB))
        if MAZINGIRABORA_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def get(self, cls, id):
        """retrieves an object of a class with id"""
        obj = None
        if cls is not None and issubclass(cls, BaseModel):
            obj = self.__session.query(cls).filter(cls.id == id).first()
        return obj

    def count(self, cls=None):
        """retrieves the number of objects of a class or all (if cls==None)"""
        return len(self.all(cls))

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

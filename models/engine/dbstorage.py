#!/usr/bin/python3


from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

from ..patient import Patient
from ..doctor import Doctor
from ..casefile import Casefile
from ..generalH import Hospital
from ..card import Card

Base = declarative_base()


class DBStorage:
    """This describe the storage for the record"""
    __engine = None
    __session = None

    def __init__(self):
        """conneect and createst the sql storage"""
        usr = "admin"
        pwd = "admin_pwd"
        db = "Medical_Record"
        host = "localhost"
        url = "{}:{}@{}/{}".format(usr, pwd, host, db)
        self.__engine = create_engine("mysql+mysqldb://{}".format(url),
                                      pool_pre_ping=True)
        meta = MetaData(bind=self.__engine)

    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the database session (self.__session)"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates and reloads content"""
        connection = self.__engine.connect()
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=connection, expire_on_commit=False)
        self.__session = scoped_session(session)

    def all(self, obj)

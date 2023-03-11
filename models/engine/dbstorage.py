#!/usr/bin/python3
"""database storage"""


from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from models.base_person import Person, Base
from models.base_institution import Institution
from models.base_record import Record
from models.patient import Patient


class DBStorage:
    """This describe the storage for the record"""
    __engine = None
    __session = None
    classes = {
            "Person": Person,
            "Record": Record,
            "Institution": Institution,
            "Patient": Patient
            }

    def __init__(self):
        """conneect and createst the sql storage"""
        usr = "Medics"
        pwd = "Medics123"
        db = "Medical_Record"
        host = "localhost"
        url = "{}:{}@{}/{}".format(usr, pwd, host, db)
        self.__engine = create_engine("mysql+mysqlconnector://{}".format(url),
                                      pool_pre_ping=True)
        self.meta = MetaData(bind=self.__engine)


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

    def all(self, obj):
        """returns all objects or all specifics"""
        classes = self.classes
        obj_dicts = {}
        print(obj)
        if obj is None:
            for item in classes:
                if obj is None or obj is classes[item] or obj is item:
                    clss = self.__session.query(classes[item]).all()
                else:
                    continue
                for objects in clss:
                    key = objects.__class__.__name__ + "." + objects.id
                    obj_dicts.update({key: objects})
        return obj_dicts

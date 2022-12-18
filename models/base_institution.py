#!/usr/bin/python3
"""
This module contains the class that descirbes the base
properties of institutions in this application.
"""


import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship

Base = declarative_base()

class Institution:
    """
    This class contains the basic properties of institution
    connecting the patient and medical staff
    """

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    name = Column(String(128), nullable=False)
    specialization = Column(String(128), nullable=False)
    records = relationship("Record", backref="institution")


    def __init__(self, *args, **kwargs):
        """This initializes the class"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            try:
                self.id = args[0]
                self.created_at = args[1]
                self.updated_at = args[2]
            except Exception:
                pass
        else:
            if "id" not in kwargs.keys():
                self.id = str(uuid.uuid4())
            try:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            except:
                pass
            finally:
                self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """converts to dictionary"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]
        return dictionary

    def save(self):
        """save to database"""
        self.updated_at = datetime.now()

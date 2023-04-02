#!/usr/bin/python3
"""
This module contains the class that descirbes the base
properties of institutions in this application.
"""


import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from typing import Dict
from sqlalchemy.orm.exc import NoResultFound

from models.base_person import Base

Base = Base

class Institution:
    """
    This class contains the basic properties of institution
    connecting the patient and medical staff
    """

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    name = Column(String(128), nullable=False)
    code = Column(String(20), unique=True, nullable=False)

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
        from models import storage
        storage.new(self)

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
        from models import storage
        self.createRecord()
        storage.save()

    def show_all(self):
        """show all intances"""
        from models import storage
        storage.reload()
        institution = storage.all(self)
        return institution

#    @setattr
    def instcode(self, value):
        """sets value of institution"""
        try:
            int(value)
        except Exception:
            raise ValueError("Value must be a number")
        self.code = value

    @classmethod
    def inst_by_id(self, id:str=None) -> Dict:
        """returns user instance by id"""
        from models import storage
        try:
            me = storage.user_by_id(self, id)
        except NoResultFound:
            return None
        return me

    @classmethod
    def search_by_code(self, code ) -> str:
        """search by code return id"""
        from models import storage
        try:
            my_id = storage.search(self, code=code)
        except NoResultFound:
            return None
        
        return my_id[0].get("id")

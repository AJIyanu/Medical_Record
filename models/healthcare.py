#!/usr/bin/python3
"""
This module contains the class that descirbes the base
properties of records in this application.
"""


import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey
from models.base_person import Base
from sqlalchemy.orm.exc import NoResultFound
from typing import Dict

class H_Facilities(Base):
    """table for all healthcare producing facilities"""
    __tablename__ = "HealthCareFacilities"
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    name = Column(String(60), nullable=False)
    maternity = Column(String(60), ForeignKey("Maternity.id"))
    general = Column(String(60), ForeignKey("Hospital.id"))

    def __init__(self, *args, **kwargs) -> None:
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
        if self.maternity is None and self.general is None:
            raise AttributeError("maternity and general can't be null")
        storage.save()

    @classmethod
    def inst_by_id(self, id) -> None:
        """returns instituion dict by health id"""
        from models import storage
        try:
            me = storage.user_by_id(self, id)
        except NoResultFound:
            return None
        from models.generalH import Hospital
        from models.maternity import Maternity
        mat = Maternity.inst_by_id(me['maternity'])
        hosp = Hospital.inst_by_id(me['general'])
        return mat if mat is not None else hosp

    @classmethod
    def inst_by_code(self, code) -> dict:
        """returns institution from code"""
        from models.generalH import Hospital
        from models.maternity import Maternity
        if code[:3] == "MAT":
            return Maternity.search_by_code(code)
        elif code[:3] == "GHP":
            return HOspital.search_by_code(code)
        return None

#!/usr/bin/python3
"""
This module contains the class that descirbes the base
properties of users of this application.
"""


import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm.exc import NoResultFound
from typing import Dict

Base = declarative_base()


class Person(Base):
    """
    This class describes the basic attribute of every
    human users
    """

    __tablename__ = "allpersons"
    __mapper_args__ = {'polymorphic_identity': 'allpersons',
                       'polymorphic_on': 'personality'}
    personality = Column(String(15))
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    firstname = Column(String(128), nullable=False)
    surname = Column(String(128), nullable=False)
    middlename = Column(String(128))
    phone = Column(String(20))
    __nin = Column(String(12), nullable=False, unique=True)
    nextofkinnin = Column(String(12))
    address = Column(String(128))
    sex = Column(String(15), nullable=False)
    dob = Column(DateTime, nullable=False)


    def __init__(self, *args, **kwargs):
        """
        initializes the class
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            try:
                self.id = args[0]
                self.surname = args[1]
                self.firstname = args[2]
                self.middlename = args[3]
            except Exception:
                pass
        else:
            if "id" not in kwargs.keys():
                self.id = str(uuid.uuid4())
            try:
                kwargs['dob'] = datetime.strptime(kwargs['dob'], '%Y-%m-%d')
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            except KeyError:
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
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
        try:
            dictionary['dob'] = self.dob.isoformat()
        except:
            pass
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]
        return dictionary

    def save(self):
        """save to database"""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def show_all(self):
        """show all intances"""
        from models import storage
        storage.reload()
        patients = storage.all(self)
        return patients

    @classmethod
    def user_by_id(self, id:str = None) -> Dict:
        """returns user instance by id"""
        from models import storage
        try:
            me = storage.user_by_id(self, id)
        except NoResultFound:
            return None
        return me

    @classmethod
    def update_me(self, id: str, **kwargs) -> None:
        """update class"""
        from models import storage
        try:
            me = storage.cls_by_id(self, id)
        except NoResultFound:
            return None
        me_lst = dir(me)
        for key in kwargs:
            if key[:2] != "__" and key in me_lst:
                setattr(me, key, kwargs[key])
        me.save()
        return

    @classmethod
    def user_by_nin(self, nin):
        """get user by nin number"""
        from models import storage
        try:
            int(nin)
        except ValueError as msg:
            raise ValueError("NIN must be a number") from msg
        if len(nin) != 11:
            raise ValueError("NIN must be 11 digits")
        user = storage.search(self, {'_Person__nin': nin})
        return user[0]

    @property
    def nin(self):
        """returns NIN"""
        return self.__nin

    @nin.setter
    def nin(self, value):
        """sets NIN value and make sure it exists"""
        if value is None:
            return
        try:
            int(value)
        except ValueError as msg:
            raise ValueError("NIN must be a number") from msg
        if len(value) != 11:
            raise ValueError("NIN must be 11 digits")
        self.__nin = value

    def purge(self):
        """deletes object"""
        from models import storage
        storage.delete(self)

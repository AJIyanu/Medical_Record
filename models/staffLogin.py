#!/usr/bin/env python3
"""Staff log in for a database table"""


from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from models.base_person import Base
from models.doctor import Doctor
import json


class Staff(Base):
    """User for a database table named users"""
    __tablename__ = "staffLogin"

    email = Column(String(60), primary_key=True, unique=True)
    staff_id = Column(String(80), ForeignKey('Doctor.id'))
    hashed_password = Column(String(250), nullable=False)
    nin = Column(String(20), unique=True, nullable=False)
    auth_inst = Column(String(200), nullable=True)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __init__(self):
        """does nothing actually"""
        from models import storage
        storage.new(self)

    def to_dict(self):
        """converts to dictionary"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]
        del dictionary["hashed_password"]
        return dictionary

    def save(self):
        """save to database"""
        from models import storage
        if self.email is None or self.hashed_password is None:
            raise AttributeError("user must have email and password")
        storage.save()

    @classmethod
    def search(self, **kwargs) -> None:
        """returns instituion dict by health id"""
        from models import storage
        diction = {}
        try:
            diction['nin'] = kwargs['nin']
        except KeyError:
            pass
        try:
            diction['email'] = kwargs['email']
        except KeyError:
            pass
        if len(diction) == 0:
            raise AttributeError("neither email or nin found")
        try:
            return storage.search(self, kwargs)[0]
        except NoResultFound:
            return None

    @classmethod
    def get_user(self, clsdict, pwd):
        """returns validated user"""
        from models import storage
        chk = storage.validate_user(self, pwd, clsdict)
        return storage.user_by_id(Doctor, clsdict['staff_id']) if chk else None

    @classmethod
    def validate_inst_code(self, id, code) -> bool:
        """returns true if user has code"""
        from models import storage
        try:
            user = storage.user_by_id(self, id)
        except NoResultFound:
            return False
        codes = json.loads(user.get("auth_inst"))
        return True if code in codes else False

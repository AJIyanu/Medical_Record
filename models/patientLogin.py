#!/usr/bin/env python3
"""User log in for a database table"""


from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from models.base_person import Base
from models.patient import Patient
from sqlalchemy.orm.exc import NoResultFound
import uuid


class User(Base):
    """User for a database table named users"""
    __tablename__ = "patientLogin"

    email = Column(String(60), primary_key=True, unique=True)
    user_id = Column(String(80), ForeignKey('Patient.id'))
    hashed_password = Column(String(250), nullable=False)
    nin = Column(String(20), unique=True, nullable=False)
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
            diction['user_id'] = kwargs['user_id']
        except KeyError:
            pass
        try:
            diction['email'] = kwargs['email']
        except KeyError:
            pass
        if len(diction) == 0:
            raise AttributeError("neither email or user_id found")
        try:
            return storage.search(self, kwargs)[0]
        except NoResultFound:
            return None

    @classmethod
    def get_user(self, clsdict, pwd):
        """returns validated user"""
        from models import storage
        chk = storage.validate_user(self, pwd, **clsdict)
        return storage.user_by_id(Patient, clsdict['user_id']) if chk else None

    @classmethod
    def reset_token(self, diction, unset: str = None) -> str:
        """returns a set token"""
        try:
            from models import storage
        except ModuleNotFoundError:
            import storage
        login = storage.login_class(self, diction)
        if unset == "set":
            login.session_id = str(uuid.uuid4())
        else:
            login.session_id = None
        login.save()
        return login.session_id

    @classmethod
    def validate_token(self, diction, token: str=None) -> bool:
        """validate token"""
        try:
            from models import storage
        except ModuleNotFoundError:
            import storage
        login = storage.login_class(self, diction)
        return token == login.session_id

    @classmethod
    def user_by_nin(self, nin):
        """gets user using NIN"""
        int(nin)
        from models import storage
        me = storage.search(self, {"nin": nin})[0]
        return storage.user_by_id(Patient, me['user_id'])


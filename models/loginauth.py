#!/usr/bin/python3
"""
This module contains the class the
represents the Login and authentifications
for all Login
"""
import uuid
# import bcrypt
from argon2 import PasswordHasher, exceptions
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm.exc import NoResultFound
from models.base_person import Base, Person


passwordhash = PasswordHasher()


class PersonAuth(Base):
    """this class defines methods to authorize all persons"""
    __tablename__ = "personauth"
    email = Column(String(60), primary_key=True, unique=True, nullable=False)
    __hashed_password = Column(String(128), nullable=False)
    person_id = Column(String(60), ForeignKey('allpersons.id'), unique=True)
    session_token = Column(String(60))
    reset_token = Column(String(60))

    def __init__(self, *args, **kwargs):
        """initialization"""
        self.__dict__.update(kwargs)
        from models import storage
        storage.new(self)

    def save(self):
        """saves instance"""
        from models import storage
        storage.save()

    def set_password(self, pwd, token: bool=False):
        """saves password"""
        if not self.reset_token and not self.__hashed_password:
            # salt = bcrypt.gensalt()
            # self.__hashed_password = bcrypt.hashpw(pwd.encode('utf-8'), salt)
            self.__hashed_password = passwordhash.hash(pwd)
        elif self.reset_token and token:
            # salt = bcrypt.gensalt()
            # self.__hashed_password = bcrypt.hashpw(pwd.encode('utf-8'), salt)
            # if self.reset_token != token:
            #     raise ValueError("Wrong token")
            """create here token validation  here otherwise compromised"""
            self.__hashed_password = passwordhash.hash(pwd)
            self.reset_token = str(uuid.uuid4())
            self.save()
        else:
            raise ValueError("Password set failed")

    def reset_password(self, pwd, token):
        """resets passowrd"""
        if token == self.reset_token:
            self.set_password(pwd, True)
        else:
            raise ValueError("not a valid token")

    def generate_token(self):
        import secrets
        import string
        alphabet = string.ascii_letters + string.digits
        self.reset_token = ''.join(secrets.choice(alphabet) for i in range(11))
        self.save()
        return self.reset_token

    def login(self, pwd):
        """returns person class"""
        # try:
        #     chck = bcrypt.checkpw(pwd.encode('utf-8'),
        #                           self.__hashed_password.encode('utf-8'))
        # except AttributeError:
        #     chck = bcrypt.checkpw(pwd.encode('utf-8'),
        #                           self.__hashed_password)
        try:
            chck = passwordhash.verify(self.__hashed_password, pwd)
        except exceptions.VerifyMismatchError:
            chck = None
        if chck:
            diction = Person.user_by_id(self.person_id)
            self.session_token = str(uuid.uuid4())
            dict.update({"session": self.session_token})
            self.save()
            return diction
        raise ValueError('incorrect password')

    def logout(self):
        """log me out"""
        self.session_token = None
        self.save()

    @classmethod
    def validate_session(self, session):
        """returns class without log in"""
        from models import storage
        if session is None:
            return
        try:
            me = storage.login_class(self, {"session_token": session})
        except NoResultFound as msg:
            raise ValueError("Session not valid") from msg
        return Person.user_by_id(me.person_id)

    @classmethod
    def find_me(self, user):
        """returns user login class"""
        from models import storage
        if "@" in user:
            try:
                return storage.login_class(self, {"email": user})
            except NoResultFound:
                return
        try:
            return storage.login_class(self, {"person_id": user})
        except NoResultFound:
            return

    @classmethod
    def jwt_auth(self, userid):
        """returns class dict"""
        return Person.user_by_id(userid)

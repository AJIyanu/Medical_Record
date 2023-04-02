#!/usr/bin/env python3
"""auth class module"""

import os
import sys


from models.staffLogin import Staff
from models.patientLogin import User


class Auth:
    """Auth"""

    __user = {}
    __login = {}

    def __init__(self):
        """does nothing"""
        pass

    def log_in(self, **kwargs) -> bool:
        """verify login data"""
        try:
            login = Staff.search(email=kwargs['email'])
            self.__login[login.get('email')] = login
        except AttributeError:
            return False
        details = Staff.get_user(kwargs['pwd'], login)
        if details is None:
            return False
        self.__user[login.get('staff_id')] = details
        if not Staff.validate_inst_code(login, kwargs["code"]):
            raise ValueError("You are not authorized in this institution")
        return True

    def create_session(self, email) -> str:
        """returns session id"""
        login = self.__login.get(email)
        if login is not None:
            del login['session_id']
            del login['__class__']
            return Staff.reset_token(login, "set")
        return None

    def delete_session(self, email) -> None:
        """deletes session for log out"""
        login = self.__login.get(email)
        if login is not None:
            del login['session_id']
            del login['__class__']
            Staff.reset_token(login)

    def validate_login(self, email, token) -> bool:
        """checks user is logged in"""
        login = self.__login.get(email)
        if login is not None:
            return Staff.validate_token(login, token)
        return False

    def staff_id(self, email):
        """returns logged in staffid"""
        staff = self.__login.get(email)
        if staff is not None:
            return staff.get("staff_id")
        return None

    def get_staff(self, userid) -> dict:
        """returns the dictionary of staff"""
        staff = self.__user.get(userid)
        if staff is None:
            return {"msg": "not logged in"}
        return staff

class Authpat:
    """authirizes patient"""

    __login = {}
    __user = {}

    def __init__(self):
        """does nothing"""
        pass

    def log_in(self, **kwargs) -> bool:
        """verify login data"""
        try:
            login = User.search(email=kwargs['email'])
            self.__login[login.get('email')] = login
        except AttributeError as e:
            return False
        details = User.get_user(login, kwargs['pwd'])
        if details is None:
            return False
        self.__user[login.get("user_id")] = details
        return True

    def create_session(self, email) -> str:
        """returns session id"""
        login = self.__login.get(email)
        if login is not None:
            del login['session_id']
            del login['__class__']
            return User.reset_token(login, "set")
        return None

    def delete_session(self, email) -> None:
        """deletes session for log out"""
        login = self.__login.get(email)
        if login is not None:
            del login['session_id']
            del login['__class__']
            User.reset_token(login)

    def validate_login(self, email, token) -> bool:
        """checks user is logged in"""
        login = self.__login.get(email)
        if login is not None:
            return User.validate_token(login, token)
        return False

    def user_id(self, email):
        """returns logged in staffid"""
        user = self.__login.get(email)
        if user is not None:
            return user.get("user_id")
        return None

    def get_patient(self, userid) -> dict:
        """returns the dictionary of staff"""
        patient = self.__user.get(userid)
        if patient is None:
            return {"msg": "not logged in"}
        return patient

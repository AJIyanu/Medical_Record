#!/usr/bin/env python3
"""auth class module"""


from datetime import datetime, date
from sqlalchemy.orm.exc import NoResultFound
from models.loginauth import PersonAuth
from models.doctor import Doctor
from models.base_person import Person


class Auth:
    """Auth"""

    __user = {}
    __login = {}

    def __init__(self):
        """does nothing"""
        pass

    def log_in(self, **kwargs) -> dict:
        """verify login data"""
        data = PersonAuth.find_me(kwargs['email'])
        if data is None:
            raise ValueError("Email does not exist")
        objdata = data.login(kwargs['pwd'])
        self.__login.update({objdata.get('id'): objdata})
        self.__user.update({kwargs['email']: data.session_token})
        return objdata, data.session_token

    def auth_inst(self, id, code):
        """validates insitution and returns data"""
        return Doctor.validate_inst_code(id, code)

    def delete_session(self, id, email) -> None:
        """deletes session for log out"""
        login = PersonAuth.find_me(email)
        login.logout()
        self.__user.pop(email)
        self.__login.pop(id)

    def validate_login(self, email, token) -> bool:
        """checks user is logged in"""
        if self.__user.get(email) == token:
            return True
        return False

    def staff_id(self, email):
        """returns logged in staffid"""
        staff = self.__login.get(email)
        if staff is not None:
            return staff.get("staff_id")
        return None

    def get_staff(self, userid) -> dict:
        """returns the dictionary of staff"""
        staff = self.__login.get(userid)
        if staff is None:
            return {"msg": "not logged in"}
        return staff

    def get_patient_data(self, nin):
        """supllies all patient needed info"""
        data = {}
        try:
            data.update(Person.user_by_nin(nin))
        except ValueError as msg:
            return {"error": str(msg)}
        except NoResultFound:
            return {"error": "NIN not found"}
        dob = datetime.fromisoformat(data['dob'])
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        data["age"] = age
        return data


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

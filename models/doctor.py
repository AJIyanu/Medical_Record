#!/usr/bin/python3
"""
This module is for Doctors
"""
import json

try:
    from models.base_person import Person, Base
except ModuleNotFoundError:
    from base_person import Person, Base
from sqlalchemy import Column, String
#from sqlalchemy.orm import relationship


class Doctor(Person, Base):
    """this describes the property of patient"""
    __tablename__ = "doctor"
    __mapper_args__ = {'polymorphic_identity': 'doctor'}
    __specialization = Column(String(20))
    __authinst = Column(String(128))



    def __init__(self, *args, **kwargs) -> None:
        """initializes Patient"""
        super().__init__(*args, **kwargs)

    @property
    def specialization(self):
        """returns the doctor's specialization"""
        return self.__specialization

    @specialization.setter
    def specialization(self, value, speclist):
        """sets specialization for doctors"""
        if value in speclist:
            self.__specialization = value
        else:
            raise ValueError("value doesn't exist")

    @property
    def authinst(self):
        """returns list of authorized institution for doctor"""
        return json.loads(self.__authinst)

    @authinst.setter
    def authinst(self, value):
        """adds authorized institution to doctor"""
        from models.base_institution import Institution
        try:
            prev = self.authinst
        except TypeError:
            prev = []
        if Institution.search_by_code(value):
            prev.append(value)
        else:
            raise ValueError("Insititution does not exist")
        self.__authinst = json.dumps(prev)

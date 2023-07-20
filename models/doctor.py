#!/usr/bin/python3
"""
This module is for Doctors
"""
import json

try:
    from models.base_person import Person, Base
except ModuleNotFoundError:
    from base_person import Person, Base
from sqlalchemy import Column, String, ForeignKey
#from sqlalchemy.orm import relationship


class Doctor(Person, Base):
    """this describes the property of patient"""
    __tablename__ = "doctor"
    __mapper_args__ = {'polymorphic_identity': 'doctor'}
    allperson_id = Column(String(60), ForeignKey('allpersons.id'), unique=True, primary_key=True)
    __specialization = Column(String(20))
    __authinst = Column(String(128))
    # __accesscode = Column(String(15))



    def __init__(self, *args, **kwargs) -> None:
        """initializes Patient"""
        super().__init__(*args, **kwargs)

    @property
    def specialization(self):
        """returns the doctor's specialization"""
        return self.__specialization

    @specialization.setter
    def specialization(self, value):
        """sets specialization for doctors"""
        if value is None:
            return
        self.__specialization = value

    @property
    def authinst(self):
        """returns list of authorized institution for doctor"""
        try:
            return json.loads(self.__authinst)
        except TypeError:
            return []

    @authinst.setter
    def authinst(self, value):
        """adds authorized institution to doctor"""
        from models.base_institution import Institution
        if value is None:
            return
        try:
            prev = self.authinst
        except TypeError:
            prev = []
        if Institution.search_by_code(value):
            prev.append(value)
        else:
            raise ValueError("Insititution does not exist")
        self.__authinst = json.dumps(prev)

    # @property
    # def accesscode(self):
    #     """returns users access code"""
    #     return self.__accesscode



    @classmethod
    def validate_inst_code(self, id, code):
        """if Doctor is authorized return True else False"""
        from models import storage
        user = storage.cls_by_id(self, id)
        return True if code in user.authinst else False

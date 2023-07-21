#!/usr/bin/python3
"""
This module is for patients
"""
from sqlalchemy import Column, String, ForeignKey

from models.base_person import Person, Base
import json
#from sqlalchemy.orm import relationship
#from models.base_record import Record


class Nurse(Person, Base):
    """this describes the property of patient"""
    __tablename__ = "nurses"
    occupation = Column(String(60))
    insurance = Column(String(25))
    __mapper_args__ = {'polymorphic_identity': 'nurses'}
    allperson_id = Column(String(60), ForeignKey('allpersons.id'), unique=True, primary_key=True)
    __authinst = Column(String(128))


    def __init__(self, *args, **kwargs) -> None:
        """initializes Patient"""
        super().__init__(*args, **kwargs)

    
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


    @classmethod
    def validate_inst_code(self, id, code):
        """if Doctor is authorized return True else False"""
        from models import storage
        user = storage.cls_by_id(self, id)
        return True if code in user.authinst else False

    @classmethod
    def update_me(self, id, key, value):
        """uodates data in base"""
        from models import storage
        user = storage.cls_by_id(self, id)
        if user is not None:
            setattr(user, key, value)
            if key == "authinst":
                user.authinst = value
            if key == "nin":
                user.nin = value
            user.save()
            return "updated"
        return "error: couldnt update"

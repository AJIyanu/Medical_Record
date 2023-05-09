#!/usr/bin/python3
"""
This module is for patients
"""
from sqlalchemy import Column, String

from models.base_person import Person, Base
#from sqlalchemy.orm import relationship
#from models.base_record import Record


class Patient(Person, Base):
    """this describes the property of patient"""
    __tablename__ = "patient"
    occupation = Column(String(60))
    insurance = Column(String(25))
    __mapper_args__ = {'polymorphic_identity': 'patient'}

    def __init__(self, *args, **kwargs) -> None:
        """initializes Patient"""
        super().__init__(*args, **kwargs)

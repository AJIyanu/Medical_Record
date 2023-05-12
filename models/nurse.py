#!/usr/bin/python3
"""
This module is for patients
"""
from sqlalchemy import Column, String, ForeignKey

from models.base_person import Person, Base
#from sqlalchemy.orm import relationship
#from models.base_record import Record


class Nurse(Person, Base):
    """this describes the property of patient"""
    __tablename__ = "nurses"
    occupation = Column(String(60))
    insurance = Column(String(25))
    __mapper_args__ = {'polymorphic_identity': 'nurses'}
    allperson_id = Column(String(60), ForeignKey('allpersons.id'), unique=True, primary_key=True)


    def __init__(self, *args, **kwargs) -> None:
        """initializes Patient"""
        super().__init__(*args, **kwargs)

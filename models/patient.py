#!/usr/bin/python3
"""
This module is for patients
"""
from models.base_person import Person, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
#from models.base_record import Record


class Patient(Person, Base):
    """this describes the property of patient"""
    __tablename__ = "Patient"
    occupation = Column(String(60))
    address = Column(String(1024))
    nxt_of_kin = Column(String(256))
    #nok_id = Column(String(60), ForeignKey("patient.id"))
    phone = Column(String(20))

    def __init__(self, *args, **kwargs) -> None:
        """initializes Patient"""
        super().__init__(*args, **kwargs)

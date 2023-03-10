#!/usr/bin/python3
"""
This module is for patients
"""
from models.base_person import Person, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class Patient(Person):
    """this describes the property of patient"""
    occupation = Column(String(60))
    address = Column(String(1024))
    nxt_of_kin = Column(String(256))
    nok_id = Column(String(60), ForeignKey("patient.id"))
    phone = Column(String(20))
    records = relationship("Record", backref="patient", cascade="all, delete")

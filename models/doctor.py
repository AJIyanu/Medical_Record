#!/usr/bin/python3
"""
This module is for Doctors
"""
from models.base_person import Person, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class Doctor(Person, Base):
    """this describes the property of patient"""
    __tablename__ = "Doctor"
    address = Column(String(1024))
    nxt_of_kin = Column(String(256))
    #nok_id = Column(String(60), ForeignKey("patient.id"))
    phone = Column(String(20))
    
    def __init__(self, *args, **kwargs) -> None:
        """initializes Patient"""
        super().__init__(*args, **kwargs)

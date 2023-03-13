#!/usr/bin/python3
"""
This module is for general Hospital
"""
from models.base_person import Base
from models.base_institution import Institution
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.healthcare import H_Facilities


class Maternity(Institution, Base):
    """this describes the property of patient"""
    __tablename__ = "Maternity"
    address = Column(String(1024))
    HealthCareFacilities = relationship("H_Facilities", backref="matern")
    facil = ""

    def __init__(self, *args, **kwargs) -> None:
        """initializes Hospital"""
        super().__init__(*args, **kwargs)

    def createRecord(self) -> None:
        """bla bla bla"""
        record = H_Facilities()
        record.maternity = self.id
        record.name = self.name
        record.save()
        self.facil = record.id

#!/usr/bin/python3
"""
This module is for general Hospital
"""
from models.base_person import Base
from models.base_institution import Institution
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.healthcare import H_Facilities

Base = Base


class Hospital(Institution, Base):
    """this describes the property of patient"""
    __tablename__ = "Hospital"
    address = Column(String(1024))
    HealthCareFacilities = relationship("H_Facilities", backref="genhpsptl")
    facil = ""

    def __init__(self, *args, **kwargs) -> None:
        """initializes Hospital"""
        super().__init__(*args, **kwargs)

    def createRecord(self) -> None:
        """creates record to database"""
        record = H_Facilities()
        record.name = self.name
        record.general = self.id
        record.save()
        self.facil = record.id

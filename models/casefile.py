#!/usr/bin/python3
"""
This module contains the class that descirbes the base
properties of records in this application.
"""


import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey
from models.base_record import Record
from models.base_person import Base

class caseFile(Record, Base):
    """
    This is just the basic information
    for general purpose
    """
    
    __tablename__ = "CaseFile"
    symptoms = Column(String(128), nullable=False)
    diagnosis = Column(String(128), nullable=False)
    prescription = Column(String(128), nullable=False)
    testResult = Column(String(128))

    def __init__(self, *args, **kwargs) -> None:
        """initializes casefile"""
        super().__init__(*args, **kwargs)

#!/usr/bin/python3
"""
This module contains the class that descirbes the base
properties of records in this application.
"""


import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, ForeignKey

Base = declarative_base()


class Record:
    """This class contains the basic properties of every
    record made connecting the patient and the doctor"""

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    staff_id = Column(String(60), ForeignKey("person.id"), nullable=False)
    patient_id = Column(String(60), ForeignKey("patient.id"), nullable=False)
    institution_id = Column(String(60), ForeignKey("institution.id"), nullable=False)

    def __init__(self, *args, **kwargs):
        """This initializes the class"""
        

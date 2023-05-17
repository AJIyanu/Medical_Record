#!/usr/bin/python3
"""
This module contains the class that descirbes the base
properties of records in this application.
"""


from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
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
    staff_id = Column(String(60), ForeignKey("doctor.allperson_id"), nullable=False)
    patient_id = Column(String(60), ForeignKey("patient.allperson_id"), nullable=False)
    doctor, patient = relationship('Doctor'), relationship('Patient')
    healthcare_id = Column(String(60), ForeignKey("institution.id"), nullable=False)

    def __init__(self, *args, **kwargs) -> None:
        """initializes casefile"""
        super().__init__(*args, **kwargs)

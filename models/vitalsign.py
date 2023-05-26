#!/usr/bin/python3
"""
This module contains the class that descirbes the base
properties of records in this application.
"""


from sqlalchemy import Column, String, ForeignKey, Integer, Index
from sqlalchemy.orm import relationship
from models.base_record import Record
from models.base_person import Base

class VitalSign(Record, Base):
    """
    This is just the basic information
    for general purpose
    """

    __tablename__ = "vitalsign"
    __table_args__ = (Index('idx_patient_id', 'patient_id'),)
    systolic = Column(Integer(), nullable=False)
    diastolic = Column(Integer(), nullable=False)
    weight = Column(Integer(), nullable=False)
    temp = Column(Integer())
    hrtbt = Column(Integer(), nullable=False)
    resprt = Column(Integer())
    oxygen = Column(Integer(), nullable=False)
    staff_id = Column(String(60), ForeignKey("nurses.allperson_id"), nullable=False)
    patient_id = Column(String(60), ForeignKey("patient.allperson_id"), nullable=False)
    nurse, patient = relationship('Nurse'), relationship('Patient')
    healthcare_id = Column(String(60), ForeignKey("institution.id"), nullable=False)

    def __init__(self, *args, **kwargs) -> None:
        """initializes casefile"""
        super().__init__(*args, **kwargs)

    

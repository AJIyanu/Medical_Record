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

class Appointment(Record, Base):
    """
    This is just the basic information
    for general purpose
    """

    __tablename__ = "Appointment_Schedule"

    # def __init__(self, *args, **kwargs) -> None:
    #     """initializes appointment book"""
    #     super().__init__(*args, **kwargs)

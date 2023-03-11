#!/usr/bin/python3
"""
This module contains the class that descirbes the base
properties of records in this application.
"""


import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, ForeignKey
from models.base_record import Record, Base

class Card(Record, Base):
    """
    This is just the basic information
    for general purpose
    """
    

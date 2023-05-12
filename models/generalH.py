#!/usr/bin/python3
"""
This module is for general Hospital
"""
from sqlalchemy import Column, String, ForeignKey

from models.base_person import Base
from models.base_institution import Institution
# from sqlalchemy.orm import relationship
# from models.healthcare import H_Facilities



class Hospital(Institution, Base):
    """this describes the property of patient"""
    __tablename__ = "hospital"
    __mapper_args__ = {'polymorphic_identity': 'hospital'}
    hosp_id = Column(String(60), ForeignKey('institution.id'), unique=True, primary_key=True)

    def __init__(self, *args, **kwargs) -> None:
        """initializes Hospital"""
        super().__init__(*args, **kwargs)

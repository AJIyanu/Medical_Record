#!/usr/bin/python3
"""
This module is for general Hospital
"""
from models.base_person import Base
from models.base_institution import Institution
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class Maternity(Institution, Base):
    """this describes the property of patient"""
    __tablename__ = "maternity"
    __mapper_args__ = {'polymorphic_identity': 'maternity'}
    maternity_id = Column(String(30), ForeignKey('institution.id'), unique=True, primary_key=True)


    def __init__(self, *args, **kwargs) -> None:
        """initializes Hospital"""
        super().__init__(*args, **kwargs)

#!/usr/bin/python3
"""
This module describes the permission tables and levels
"""
from enum import  Enum
from sqlalchemy import Column, String, Enum as EnumType, Integer
from sqlalchemy.schema import DefaultClause
from base_person import Base


class AllowedValues(Enum):
    """Constrain value for permision"""
    NOPERM = 0
    VIEW = 1
    EDIT = 11

class constraints:
    id = Column(Integer, primary_key=True)

    @classmethod
    def __declare_last__(cls):
        for column in cls.__table__.columns:
            if not column.primary_key:
                column.default = DefaultClause(str(AllowedValues.ZERO.value))
                column.server_default = DefaultClause(str(AllowedValues.ZERO.value))
                column.server_onupdate = DefaultClause(str(AllowedValues.ZERO.value))

class Permissions(constraints, Base):
    """permission table"""

    __tablename__ = "Permissions"

    id = Column(String(15), primary_key=True)
    casefile = Column(EnumType(AllowedValues), nullable=False)
    vitalsign = Column(EnumType(AllowedValues), nullable=False)

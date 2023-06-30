#!/usr/bin/python3
"""
This module describes the permission tables and levels
"""
from sqlalchemy import Column, String, Enum as EnumType, Integer
from sqlalchemy.schema import DefaultClause
from models.base_person import Base
from sqlalchemy.orm.exc import NoResultFound


class constraints:
    id = Column(Integer, primary_key=True)

    @classmethod
    def __declare_last__(cls):
        for column in cls.__table__.columns:
            if not column.primary_key:
                column.default = DefaultClause(0)
                column.server_default = DefaultClause(0)
                column.server_onupdate = DefaultClause(0)

class Permissions(Base):
    """permission table"""

    __tablename__ = "Permissions"

    id = Column(String(15), primary_key=True)
    casefile = Column(EnumType(0, 1, 11), default=0, nullable=False)
    vitalsign = Column(EnumType(0, 1, 11), default=0, nullable=False)


    def __init__(self, *args, **kwargs):
        """initializes permission"""
        if args:
            self.id = args[0]
            try:
                val = str(int(args[0]))
            except ValueError:
                return
            except IndexError:
                return
        elif kwargs:
            if "id" in kwargs:
                self.id = kwargs['id']
            perm = [x.name for x in self.__table__.columns]
            for key in kwargs:
                if key in perm:
                    code = kwargs[key]
                    if code == 0 or code == 1 or code == 11:
                        setattr(self, key, kwargs[key])
        from models import storage
        storage.new(self)

    def save(self):
        """saves instance"""
        from models import storage
        storage.save()

    def transform(self, code):
        """returns the boolen equ"""
        if code == 0 or code == "0":
            return [False, False]
        if code == 1 or code == "1" or code == "01":
            return [False, True]
        if code == 3 or code == "3" or code == 11:
            return [True, True]
        return [False, False]

    def set_permission(self, perm, code):
        """sets permision for class"""
        try:
            code = int(code)
        except ValueError:
            return "valueerror"
        if code != 0 and code != 1 and code != 11:
            return "invalid"
        for x in self.__table__.columns:
            if x.name == perm:
                print("match found")
                setattr(self, perm, code)

    def all_permissions(self):
        """returns all permision I have"""
        diction = {'id': self.id}
        for x in self.__table__.columns:
            if x.name != 'id':
                val = getattr(self, x.name)
                val = self.transform(val)
                diction.update({x.name: val})
        return diction

    def permission(self, permit, permtype=None):
        """
        returns true or false for view, edit, all
        and list of permission for spec permission
        """
        if permtype is None:
            val = getattr(self, permit)
            return self.transform(val)
        if permtype == "view":
            if getattr(self, permit) == 1:
                return True
            if getattr(self, permit) == 11:
                return True
            return False
        if permtype == "edit" or permtype == "all":
            if getattr(self, permit) == 11:
                return True
            return False
        return False

    @classmethod
    def me(self, role):
        """returns the instance of role itself"""
        from models import storage
        try:
            return storage.login_class(self, {"id": role})
        except NoResultFound:
            return None

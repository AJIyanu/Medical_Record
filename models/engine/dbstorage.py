#!/usr/bin/python3
"""database storage"""

from typing import Dict, List

from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.exc import NoResultFound

from models.base_person import Person, Base
from models.casefile import caseFile
from models.patient import Patient
from models.doctor import Doctor
from models.generalH import Hospital
from models.maternity import Maternity
from models.card import Appointment
from models.loginauth import PersonAuth
from models.nurse import Nurse
from models.vitalsign import VitalSign
from models.permissions import Permissions


class DBStorage:
    """This describe the storage for the record"""
    __engine = None
    __session = None
    classes = {
               "Patient": Patient,
               "Doctor": Doctor,
               "generalH": Hospital,
               "Maternity": Maternity,
               "Casefile": caseFile,
               "Person": Person,
               "Appointment": Appointment,
               "PersonAuth": PersonAuth,
               "Nurses": Nurse,
               "VitalSign": VitalSign,
               "Permissions" : Permissions
               }

    def __init__(self):
        """conneect and createst the sql storage"""
        usr = "Medics"
        pwd = "Medics123"
        db = "Medical_Record"
        host = "localhost"
        url = "{}:{}@{}/{}".format(usr, pwd, host, db)
        self.__engine = create_engine("mysql+mysqlconnector://{}".format(url),
                                      pool_size=10, pool_pre_ping=True)


    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the database session (self.__session)"""
        self.__session.commit()
        # self.__session.close()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)
            self.__session.commit()
            self.__session.flush()

    def reload(self):
        """creates and reloads content"""
        connection = self.__engine.connect()
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=connection, expire_on_commit=False)
        self.__session = scoped_session(session)

    def all(self, obj=None):
        """returns all objects or all specifics"""
        classes = self.classes
        obj_dicts = {}
        for item in classes:
            if obj is None or obj == item or type(obj) == classes[item]:
                clss = self.__session.query(classes[item]).all()
            else:
                continue
            for objects in clss:
                try:
                    key = objects.__class__.__name__ + "." + objects.id
                except AttributeError:
                    key = objects.__class__.__name__ + "." + objects.email
                obj_dicts.update({key: objects})
        return obj_dicts

    def close(self):
        """closes session"""
        self.__session.remove()


    def print_changes(self):
        """prints changes to be committed"""
        for obj in self.__session.dirty:
            print(obj)
        else:
            print("no changes yet")

    def user_by_id(self, obj=None, id: str = None) -> Dict:
        """finds user by id"""
        if obj is None:
            return
        Session = self.__session
        query = Session.query(obj).filter_by(id=id)
        if query.first() is None:
            raise NoResultFound
        data = query.first()
        return data.to_dict()

    def cls_by_id(self, obj=None, id: str = None) -> Dict:
        """returns user class by id"""
        if obj == None:
            return
        Session = self.__session
        query = Session.query(obj).filter_by(id=id)
        if query.first() is None:
            raise NoResultFound
        data = query.first()
        return data

    def search(self, obj=None, **kwargs) -> List[Dict]:
        """search out list of users"""
        Session = self.__session
        if isinstance(obj, str):
            obj = self.classes.get(obj)
        if obj is None or kwargs is None:
            return
        query = Session.query(obj).filter_by(**kwargs)
        if query.first() is None:
            raise NoResultFound
        return [data for data in query]

    # def validate_user(self, obj=None, pwd=None,  **kwargs: Dict) -> bool:
    #     """validate user"""
    #     if obj is None:
    #         return None
    #     Session = self.__session
    #     diction = {}
    #     try:
    #         diction["nin"] = kwargs["nin"]
    #     except KeyError:
    #         pass
    #     try:
    #         diction["email"] = kwargs["email"]
    #     except KeyError:
    #         pass
    #     if len(diction) == 0:
    #         return False
    #     query = Session.query(obj).filter_by(**diction)
    #     query = query.first()
    #     if query == None:
    #         return False
    #     return True if query.hashed_password == pwd else False

    def login_class(self, obj=None, kwargs: Dict=None) -> List[Dict]:
        """search out list of users"""
        if obj is None or kwargs is None:
            return
        Session = self.__session
        query = Session.query(obj).filter_by(**kwargs)
        if query.first() is None:
            raise NoResultFound
        return query.first()

    def search_by_order(self, obj, all: bool=False, diction: bool=True, **kwargs):
        """returns objects in an order it is inserted"""
        if isinstance(obj, str):
            obj = self.classes.get(obj)
        if obj is None or kwargs is None:
            return
        Session =self.__session
        query = Session.query(obj).filter_by(**kwargs).order_by(desc(obj.created_at))
        # print(query.all())
        if not query.first():
            raise NoResultFound
        if all:
            return query.all() if not diction else [user.to_dict() for user in query.all()]
        return query.first() if not diction else query.first().to_dict()
        
    @property
    def temp_session(self):
        """temp returns session"""
        return self.__session
        
    def joint_request(self, **rel):
        """
        obj_a for first class
        obj_b for second class
        rel_a for first relationship
        rel_b for second relationship
        
        returns a joint request tuple
        """
        ses = self.__session
        for check in ["obj_a", "obj_b", "rel_a", "rel_b"]:
            if check not in rel:
                return None
            if isinstance(rel[check], str):
                rel[check] = self.classes.get(rel[check])
            if rel[check] is None:
                return None
        que = ses.query(rel['obj_a'], rel['obj_b']).join(rel['obj_b'],
                        rel['rel_b'] == rel['rel_a'])
        if not que.first():
            raise NoResultFound
        return que.all()

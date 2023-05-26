# pylint: disable=import-outside-toplevel
#!/usr/bin/python3
"""
This module contains the class that descirbes the base
properties of records in this application.
"""


import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime #ForeignKey
from models.base_person import Base
from typing import Dict, List
from sqlalchemy.orm.exc import NoResultFound



class Record:
    """This class contains the basic properties of every
    record made connecting the patient and the doctor"""

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    #staff_id = Column(String(60), ForeignKey("Doctor.id"), nullable=False)
    #patient_id = Column(String(60), ForeignKey("Patient.id"), nullable=False)
    #healthcare_id = Column(String(60), ForeignKey("HealthCareFacilities.id"), nullable=False)

    def __init__(self, *args, **kwargs):
        """This initializes the class"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            try:
                self.id = args[0]
                self.created_at = args[1]
                self.updated_at = args[2]
            except IndexError:
                pass
        else:
            if "id" not in kwargs.keys():
                self.id = str(uuid.uuid4())
            try:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            except KeyError:
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
            finally:
                self.__dict__.update(kwargs)
        from models import storage
        storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """converts to dictionary"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]
        return dictionary

    def save(self):
        """save to database"""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def show_all(self):
        """show all intances"""
        from models import storage
        storage.reload()
        record = storage.all(self)
        return record

    @classmethod
    def user_by_id(self, myid:str = None) -> Dict:
        """returns user instance by id"""
        from models import storage
        try:
            me = storage.user_by_id(self, myid)
        except NoResultFound:
            return None
        return me

    @classmethod
    def search_patient(self, **kwargs) -> List[Dict]:
        """search patient's record"""
        diction = {}
        try:
            diction.update({'patient_id': kwargs['patient_id']})
        except KeyError as exe:
            raise KeyError("You must supply <patient_id>") from exe
        try:
            diction.update({'healthcare_id': kwargs['healthcare_id']})
        except KeyError:
            pass
        try:
            diction.update({'staff_id': kwargs['staff_id']})
        except KeyError:
            pass
        from models import storage
        try:
            return storage.search(self, diction)
        except NoResultFound:
            return None

    @classmethod
    def search_doctor(self, **kwargs) -> List[Dict]:
        """search doctor's record"""
        diction = {}
        try:
            diction.update({'staff_id': kwargs['staff_id']})
        except KeyError as exe:
            raise KeyError("You must supply <staff_id>") from exe
        try:
            diction.update({'healthcare_id': kwargs['healthcare_id']})
        except KeyError:
            pass
        try:
            diction.update({'patient_id': kwargs['patient_id']})
        except KeyError:
            pass
        from models import storage
        try:
            return storage.search(self, diction)
        except NoResultFound:
            return None

    @classmethod
    def update_me(self, myid: str, **kwargs) -> None:
        """update class"""
        from models import storage
        try:
            me = storage.cls_by_id(self, myid)
        except NoResultFound:
            return None
        me_lst = dir(me)
        for key in kwargs:
            if key[:2] != "__" and key in me_lst:
                setattr(me, key, kwargs[key])
        me.save()

    @classmethod
    def pat_last_saved(self, userid):
            """returns last saved data of a user"""
            from models import storage
            try:
                return storage.search_by_order(self, False, patient_id=userid)
            except NoResultFound:
                return None

    @classmethod
    def pat_record(self, userid):
            """returns last saved data of a user"""
            from models import storage
            try:
                return storage.search_by_order(self, True, patient_id=userid)
            except NoResultFound:
                return None

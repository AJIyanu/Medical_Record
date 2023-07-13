#!/usr/bin/env python3
""" Module for reister functions
"""

from models import storage

classes = storage.classes

def register_doctor(**userdata):
    """registers a doctor"""
    doctor = classes.get("Doctor")
    login = classes.get("PersonAuth")
    new_user = doctor(**userdata)
    new_user.authinst = userdata.get("authinst")
    new_user.specialization = userdata.get("specialization")
    new_user.nin = userdata.get("nin")
    try:
        new_user.save()
        status = "saved"
    except Exception:
        print("cannot save")
        status = "error"
    print(new_user.to_dict())
    new_user_auth = login()
    new_user_auth.person_id = new_user.id
    new_user_auth.email = userdata.get("email")
    new_user_auth.set_password = userdata.get("pwd")
    try:
        new_user_auth.save()
    except Exception:
        new_user.purge()
        status = "error login"
    # print(new_user_auth.to_dict())
    return status

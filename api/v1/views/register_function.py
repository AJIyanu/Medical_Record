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
        new_user_auth = login()
        new_user_auth.person_id = new_user.id
        new_user_auth.email = userdata.get("email")
        new_user_auth.set_password(userdata.get("password"))
        try:
            new_user_auth.save()
        except Exception as msgg:
            print(f"{msgg}, auth didnt save")
            new_user.purge()
            status = "error login"
    except Exception as msg:
        print(msg)
        status = "error"
    return status

def register_nurse(**userdata):
    """registers a nurse"""
    nurse = classes.get("Nurse")
    login = classes.get("PersonAuth")
    new_user = nurse(**userdata)
    new_user.nin = userdata.get("nin")
    new_user.authinst = "GENOYSK293"
#    new_user.specialization = userdata.get("specialization")
    print(userdata)
    try:
        new_user.save()
        status = "saved"
        new_user_auth = login()
        new_user_auth.person_id = new_user.id
        new_user_auth.email = userdata.get("email")
        new_user_auth.set_password(userdata.get("password"))
        try:
            new_user_auth.save()
        except Exception as msgg:
            print(f"{msgg}, auth didnt save")
            new_user.purge()
            status = "error login"
    except Exception as msg:
        print(msg)
        status = "error"
    return status
